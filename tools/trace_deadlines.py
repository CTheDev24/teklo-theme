"""Manual Trace policy queue. Reports work; never sends, refunds or deletes."""
from datetime import datetime, timedelta, timezone


def timestamp(value):
    try:
        result = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if result.tzinfo is None:
            raise ValueError('Timezone required')
        return result
    except (AttributeError, TypeError, ValueError) as exc:
        raise ValueError('ISO timestamp with timezone required') from exc


POLICY_EVENTS = {'input_requested', 'customer_replied', 'intake_usable',
                 'reminder_sent', 'item_delivered', 'cancelled_refunded', 'files_deleted'}


def record_policy(piece, event):
    """Mutates only a copied piece; assertions require independent operator evidence."""
    policy = piece.setdefault('policy', {})
    kind, at = event['type'], event['at']
    pending = policy.get('request')
    if kind == 'input_requested':
        if policy.get('closed') or piece['state'] == 'APPROVED':
            raise ValueError('Closed or approved piece cannot start an input deadline')
        if pending:
            raise ValueError('Record the customer reply before opening another request')
        if event.get('request_kind') not in ('intake', 'clarification') or not event.get('request_id'):
            raise ValueError('Request id and intake/clarification kind required')
        policy['request'] = {'id': event['request_id'], 'kind': event['request_kind'],
                             'at': at, 'reminders': []}
    elif kind == 'customer_replied':
        if not pending or event.get('request_id') != pending['id']:
            raise ValueError('Reply must identify current request')
        policy.pop('request')
    elif kind == 'intake_usable':
        if policy.get('closed') or not piece.get('route') or piece.get('missing'):
            raise ValueError('Verified route and complete intake required')
        if policy.get('usable_at'):
            raise ValueError('First proof deadline cannot be reset')
        if event.get('complete_usable_verified') is not True:
            raise ValueError('Operator must verify complete usable intake and its actual timestamp')
        usable = event.get('usable_at')
        if timestamp(usable) > timestamp(at):
            raise ValueError('Usable intake cannot be in the future')
        policy['usable_at'] = usable
    elif kind == 'reminder_sent':
        stage = event.get('stage')
        if not pending or event.get('request_id') != pending['id'] or stage not in ('48h', 'day7'):
            raise ValueError('Reminder must identify current request and stage')
        hours = 48 if stage == '48h' else 168
        if timestamp(at) < timestamp(pending['at']) + timedelta(hours=hours):
            raise ValueError('Reminder stage is not due yet')
        if stage in pending['reminders']:
            raise ValueError('Reminder stage already recorded')
        pending['reminders'].append(stage)
    elif kind in ('item_delivered', 'cancelled_refunded'):
        if policy.get('closed'):
            raise ValueError('Closure already recorded; do not reset deletion deadline')
        if kind == 'item_delivered' and not piece.get('approval'):
            raise ValueError('Written approval required before fulfilled delivery')
        if kind == 'cancelled_refunded' and event.get('full_refund_verified') is not True:
            raise ValueError('Record completed cancellation and full refund evidence first')
        policy.update(closed=kind, closed_at=at)
        policy.pop('request', None)
    elif kind == 'files_deleted':
        required = {'jotform', 'drive', 'local', 'working_files', 'proofs', 'backups'}
        if not policy.get('closed') or set(event.get('checked_locations', [])) != required:
            raise ValueError('Closure and verified deletion/reconciliation for every storage location required')
        if timestamp(at) < timestamp(policy['closed_at']):
            raise ValueError('Deletion completion cannot precede closure')
        if event.get('deletion_verified') is not True:
            raise ValueError('Independently verify deletion, including provider backup limitations')
        policy['deleted_at'] = at


def deadlines(piece, now=None):
    """UTC dates use elapsed hours/calendar days, never business-day arithmetic."""
    now = timestamp(now) if now is not None else datetime.now(timezone.utc)
    policy = piece.get('policy', {})
    tasks = []
    def add(action, start, hours):
        due = timestamp(start) + timedelta(hours=hours)
        tasks.append({'action': action, 'due_at': due.astimezone(timezone.utc).isoformat(),
                      'due': now >= due})
    if policy.get('closed'):
        if not policy.get('deleted_at'):
            add('manually_delete_customer_files_all_locations', policy['closed_at'], 14 * 24)
        return tasks
    pending = policy.get('request')
    if pending:
        age = now - timestamp(pending['at'])
        if age >= timedelta(days=10):
            add('review_no_response_cancel_and_full_refund', pending['at'], 240)
        else:
            add('customer_response_due', pending['at'], 48)
            for stage, hours in (('48h', 48), ('day7', 168)):
                if stage not in pending['reminders']:
                    add('manually_send_reminder_' + stage, pending['at'], hours)
            add('review_no_response_cancel_and_full_refund', pending['at'], 240)
    if policy.get('usable_at') and not policy.get('first_proof_sent_at'):
        add('send_first_proof', policy['usable_at'], 48)
    return tasks
