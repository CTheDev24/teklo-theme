"""Offline Trace intake/proof gate. No sending, charging or production side effects."""
import copy
import hashlib
import math
import xml.etree.ElementTree as ET
from datetime import datetime
from tools.trace_deadlines import POLICY_EVENTS, record_policy, timestamp


def validate_gpx(data):
    if len(data) > 20_000_000:
        raise ValueError('GPX exceeds validation limit')
    try:
        data.decode('utf-8-sig')
    except UnicodeDecodeError as exc:
        raise ValueError('Export GPX as UTF-8') from exc
    if b'\x00' in data:
        raise ValueError('Export GPX as UTF-8')
    if b'<!DOCTYPE' in data.upper() or b'<!ENTITY' in data.upper():
        raise ValueError('DTD/entities are not accepted')
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        raise ValueError('Malformed GPX XML') from exc
    if root.tag.split('}')[-1] != 'gpx':
        raise ValueError('Not a GPX document')
    points = []
    for point in root.iter():
        if point.tag.split('}')[-1] in ('trkpt', 'rtept'):
            try:
                lat, lon = float(point.attrib['lat']), float(point.attrib['lon'])
            except (KeyError, ValueError) as exc:
                raise ValueError('Missing or invalid coordinates') from exc
            if not math.isfinite(lat) or not math.isfinite(lon) or not (-90 <= lat <= 90 and -180 <= lon <= 180):
                raise ValueError('Invalid coordinates')
            points.append((lat, lon))
    if len(set(points)) < 2:
        raise ValueError('Route needs at least two distinct points')
    return {'sha256': hashlib.sha256(data).hexdigest(), 'points': len(points)}


def new_piece(shop, order, line, unit, quantity):
    if not all(isinstance(v, str) and v.strip() for v in (shop, order, line)):
        raise ValueError('Immutable Shopify shop/order/line identity required')
    if type(unit) is not int or type(quantity) is not int or not 1 <= unit <= quantity:
        raise ValueError('Unit outside purchased quantity')
    return {'key': [shop, order, line, unit], 'quantity': quantity, 'state': 'AWAITING_INTAKE', 'revision': 0,
            'intake': None, 'route': None, 'proof': None, 'delivery': None, 'approval': None,
            'events': []}


def transition(piece, event):
    """Caller persists output atomically, retaining source evidence outside the repo.

    This validates recorded operator evidence; it does not authenticate email or
    fetch Shopify/Jotform. Those integrations must verify identities before use.
    """
    if not isinstance(event, dict) or not isinstance(event.get('type'), str):
        raise ValueError('Event object and type required')
    p = copy.deepcopy(piece)
    kind = event['type']
    if not event.get('at') or not event.get('evidence'):
        raise ValueError('Timestamp and source evidence required')
    try:
        stamp = datetime.fromisoformat(event['at'].replace('Z', '+00:00'))
        if stamp.tzinfo is None:
            raise ValueError('Timezone required')
    except (ValueError, TypeError, AttributeError) as exc:
        raise ValueError('ISO timestamp with timezone required') from exc
    if not isinstance(event['evidence'], str) or not event['evidence'].strip():
        raise ValueError('Source evidence required')
    if p['events'] and stamp < timestamp(p['events'][-1]['at']):
        raise ValueError('Event timestamp precedes last recorded event')
    if kind in POLICY_EVENTS:
        record_policy(p, event)
        p['revision'] += 1
        p['events'].append({k:event[k] for k in ('type','at','evidence')})
        return p
    if p.get('policy', {}).get('closed'):
        raise ValueError('Closed piece cannot resume production workflow')
    if p['state'] == 'APPROVED' and kind not in ('intake', 'route', 'proof', 'correction', 'invalid_input', 'private_link', 'unavailable_course', 'color_unclear'):
        raise ValueError('Approved revision cannot be silently changed')
    if kind == 'intake':
        data = event.get('data')
        if not isinstance(data, dict):
            raise ValueError('Intake data must be an object')
        if event.get('verified_key') != p['key']:
            raise ValueError('Reconcile order email, line reference and unit to Shopify first')
        required = ('runner', 'race', 'date', 'location', 'distance', 'finish', 'accent', 'route_method')
        missing = [key for key in required if not isinstance(data.get(key), str) or not data[key].strip()]
        if (not isinstance(data.get('finish_time'), str) or not data['finish_time'].strip()) and data.get('omit_finish_time') is not True:
            missing.append('finish_time_or_explicit_omission')
        if data.get('route_method') not in ('gpx', 'activity', 'course', 'map'):
            missing.append('route_method')
        source_fields = {'gpx': ('route_source',), 'activity': ('activity_url',),
                         'course': ('course_name', 'course_year', 'course_distance', 'course_location'),
                         'map': ('route_source',)}
        missing.extend(key for key in source_fields.get(data.get('route_method'), ())
                       if not isinstance(data.get(key), str) or not data[key].strip())
        if data.get('route_method') == 'activity':
            from urllib.parse import urlsplit
            link = urlsplit(str(data.get('activity_url', '')))
            if link.scheme != 'https' or not link.hostname or link.username or link.password:
                missing.append('valid_https_activity_url')
        p.update(intake=data, route=None, proof=None, delivery=None, approval=None,
                 state='NEEDS_INPUT' if missing else 'AWAITING_ROUTE', missing=missing)
    elif kind == 'route':
        if p['state'] not in ('AWAITING_ROUTE', 'NEEDS_INPUT', 'AWAITING_PROOF', 'AWAITING_PROOF_DELIVERY', 'AWAITING_APPROVAL', 'APPROVED') or not p['intake'] or p.get('missing'):
            raise ValueError('Complete intake required')
        # All source paths converge on validated GPX + a human verification record.
        route = validate_gpx(event['gpx'])
        if event.get('source_verified') is not True:
            raise ValueError('Operator must verify course/year/distance or activity route')
        p.update(route=route, proof=None, delivery=None, approval=None, state='AWAITING_PROOF')
    elif kind == 'proof':
        if p['state'] not in ('AWAITING_PROOF', 'AWAITING_PROOF_DELIVERY', 'AWAITING_APPROVAL', 'APPROVED') or not p['route'] or p.get('missing'):
            raise ValueError('Verified route and complete intake required')
        if event.get('layout_reviewed') is not True or event.get('color_confirmed') is not True:
            raise ValueError('Check long names, layout and medal color before proof')
        if not event.get('version') or not event.get('file'):
            raise ValueError('Identified proof artifact required')
        artifact_hash = hashlib.sha256(event['file']).hexdigest()
        if any(old['version'] == event['version'] or old['sha256'] == artifact_hash
               for old in p.get('policy', {}).get('delivered_proofs', [])):
            raise ValueError('Previously delivered proof cannot restart response deadlines; record a reminder instead')
        p.update(proof={'revision':p['revision'] + 1, 'version':event['version'], 'sha256':artifact_hash,
                        'route_sha256':p['route']['sha256']}, delivery=None, approval=None,
                 state='AWAITING_PROOF_DELIVERY')
    elif kind == 'delivered':
        if p['state'] != 'AWAITING_PROOF_DELIVERY' or event.get('proof') != p['proof']:
            raise ValueError('Delivery must identify current proof')
        if not event.get('message_id') or event.get('recipient_verified') is not True:
            raise ValueError('Verified order recipient and delivery evidence required')
        policy = p.setdefault('policy', {})
        pending = policy.get('request')
        if pending and pending['kind'] != 'proof':
            raise ValueError('Record the reply to pending input before delivering a proof')
        delivered = policy.setdefault('delivered_proofs', [])
        if any(old['version'] == p['proof']['version'] or old['sha256'] == p['proof']['sha256'] for old in delivered):
            raise ValueError('Previously delivered proof cannot restart response deadlines')
        delivered.append({'version': p['proof']['version'], 'sha256': p['proof']['sha256']})
        p.update(delivery={'message_id':event['message_id'], 'evidence':event['evidence']}, state='AWAITING_APPROVAL')
        policy.setdefault('first_proof_sent_at', event['at'])
        policy['request'] = {'id': event['message_id'], 'kind': 'proof', 'at': event['at'], 'reminders': []}
    elif kind == 'approve':
        if p['state'] != 'AWAITING_APPROVAL' or event.get('proof') != p['proof'] or event.get('verified_key') != p['key']:
            raise ValueError('Approval must identify this piece and current delivered proof')
        if event.get('sender_verified') is not True or event.get('text', '').strip() != 'APPROVED FOR PRODUCTION':
            raise ValueError('Explicit written approval from verified order contact required')
        p.update(approval={'evidence':event['evidence'], 'at':event['at'], 'proof':p['proof']}, state='APPROVED')
        p.setdefault('policy', {}).pop('request', None)
    elif kind in ('invalid_input', 'private_link', 'unavailable_course', 'color_unclear', 'correction'):
        p.update(state='NEEDS_INPUT', proof=None, delivery=None, approval=None)
        p['route'] = None
    elif kind == 'no_response':
        if p['state'] not in ('AWAITING_INTAKE', 'NEEDS_INPUT', 'AWAITING_ROUTE', 'AWAITING_APPROVAL'):
            raise ValueError('Nonresponse applies only while awaiting customer input or approval')
        p.update(resume_state=p['state'], state='HOLD_NO_RESPONSE')
    elif kind == 'resume':
        if p['state'] != 'HOLD_NO_RESPONSE':
            raise ValueError('Only a nonresponse hold can resume')
        p['state'] = p.pop('resume_state')
    else:
        raise ValueError('Unknown workflow event')
    p['revision'] += 1
    p['events'].append({k:event[k] for k in ('type','at','evidence')})
    return p
