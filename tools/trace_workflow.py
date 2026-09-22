"""Offline Trace intake/proof gate. No sending, charging or production side effects."""
import copy
import hashlib
import math
import xml.etree.ElementTree as ET


def validate_gpx(data):
    if len(data) > 20_000_000:
        raise ValueError('GPX exceeds validation limit')
    if b'<!DOCTYPE' in data.upper() or b'<!ENTITY' in data.upper():
        raise ValueError('DTD/entities are not accepted')
    root = ET.fromstring(data)
    if root.tag.split('}')[-1] != 'gpx':
        raise ValueError('Not a GPX document')
    points = []
    for point in root.iter():
        if point.tag.split('}')[-1] in ('trkpt', 'rtept'):
            lat, lon = float(point.attrib['lat']), float(point.attrib['lon'])
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
    return {'key': [shop, order, line, unit], 'state': 'AWAITING_INTAKE', 'revision': 0,
            'intake': None, 'route': None, 'proof': None, 'delivery': None, 'approval': None,
            'events': []}


def transition(piece, event):
    """Caller persists output atomically, retaining source evidence outside the repo.

    This validates recorded operator evidence; it does not authenticate email or
    fetch Shopify/Jotform. Those integrations must verify identities before use.
    """
    p = copy.deepcopy(piece)
    kind = event['type']
    if not event.get('at') or not event.get('evidence'):
        raise ValueError('Timestamp and source evidence required')
    if p['state'] == 'APPROVED' and kind not in ('intake', 'route', 'proof'):
        raise ValueError('Approved revision cannot be silently changed')
    if kind == 'intake':
        data = event['data']
        if event.get('verified_key') != p['key']:
            raise ValueError('Reconcile order email, line reference and unit to Shopify first')
        required = ('runner', 'race', 'date', 'location', 'distance', 'finish', 'accent', 'route_method')
        missing = [key for key in required if not str(data.get(key, '')).strip()]
        if not data.get('finish_time') and data.get('omit_finish_time') is not True:
            missing.append('finish_time_or_explicit_omission')
        if data.get('route_method') not in ('gpx', 'activity', 'course', 'map'):
            missing.append('route_method')
        p.update(intake=data, route=None, proof=None, delivery=None, approval=None,
                 state='NEEDS_INPUT' if missing else 'AWAITING_ROUTE', missing=missing)
    elif kind == 'route':
        if p['state'] not in ('AWAITING_ROUTE', 'NEEDS_INPUT', 'AWAITING_PROOF', 'AWAITING_APPROVAL', 'APPROVED') or not p['intake'] or p.get('missing'):
            raise ValueError('Complete intake required')
        # All source paths converge on validated GPX + a human verification record.
        route = validate_gpx(event['gpx'])
        if event.get('source_verified') is not True:
            raise ValueError('Operator must verify course/year/distance or activity route')
        p.update(route=route, proof=None, delivery=None, approval=None, state='AWAITING_PROOF')
    elif kind == 'proof':
        if not p['route'] or p.get('missing'):
            raise ValueError('Verified route and complete intake required')
        if event.get('layout_reviewed') is not True or event.get('color_confirmed') is not True:
            raise ValueError('Check long names, layout and medal color before proof')
        if not event.get('version') or not event.get('file'):
            raise ValueError('Identified proof artifact required')
        p.update(proof={'revision':p['revision'] + 1, 'version':event['version'], 'sha256':hashlib.sha256(event['file']).hexdigest(),
                        'route_sha256':p['route']['sha256']}, delivery=None, approval=None,
                 state='AWAITING_PROOF_DELIVERY')
    elif kind == 'delivered':
        if p['state'] != 'AWAITING_PROOF_DELIVERY' or event.get('proof') != p['proof']:
            raise ValueError('Delivery must identify current proof')
        if not event.get('message_id') or event.get('recipient_verified') is not True:
            raise ValueError('Verified order recipient and delivery evidence required')
        p.update(delivery={'message_id':event['message_id'], 'evidence':event['evidence']}, state='AWAITING_APPROVAL')
    elif kind == 'approve':
        if p['state'] != 'AWAITING_APPROVAL' or event.get('proof') != p['proof'] or event.get('verified_key') != p['key']:
            raise ValueError('Approval must identify this piece and current delivered proof')
        if event.get('sender_verified') is not True or event.get('text', '').strip() != 'APPROVED FOR PRODUCTION':
            raise ValueError('Explicit written approval from verified order contact required')
        p.update(approval={'evidence':event['evidence'], 'at':event['at'], 'proof':p['proof']}, state='APPROVED')
    elif kind in ('invalid_input', 'private_link', 'unavailable_course', 'color_unclear', 'correction'):
        p.update(state='NEEDS_INPUT', proof=None, delivery=None, approval=None)
        if kind != 'correction':
            p['route'] = None
    elif kind == 'no_response':
        if p['state'] == 'APPROVED':
            raise ValueError('Already approved')
        # Record the follow-up need, never auto-approve/cancel/refund.
    else:
        raise ValueError('Unknown workflow event')
    p['revision'] += 1
    p['events'].append({k:event[k] for k in ('type','at','evidence')})
    return p
