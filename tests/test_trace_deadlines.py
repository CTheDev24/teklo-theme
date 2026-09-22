import unittest
from tools.trace_deadlines import deadlines
from tools.trace_workflow import new_piece, transition
from test_trace_workflow import intake, event, GPX


def ev(kind, at='2026-09-21T00:00:00Z', **kw):
    return {**event(kind, **kw), 'at': at}


class Deadlines(unittest.TestCase):
    def request(self):
        return transition(new_piece('s', 'o', 'l', 1, 1), ev(
            'input_requested', request_id='instructions', request_kind='intake'))

    def test_exact_response_reminder_and_refund_boundaries(self):
        p = self.request()
        tasks = deadlines(p, '2026-09-22T23:59:59Z')
        self.assertFalse(any(t['due'] for t in tasks))
        tasks = deadlines(p, '2026-09-23T00:00:00Z')
        self.assertEqual([t['action'] for t in tasks if t['due']],
                         ['customer_response_due', 'manually_send_reminder_48h'])
        p = transition(p, ev('reminder_sent', '2026-09-23T00:00:00Z',
                             request_id='instructions', stage='48h'))
        self.assertNotIn('manually_send_reminder_48h', [t['action'] for t in deadlines(p)])
        tasks = deadlines(p, '2026-09-28T00:00:00Z')
        self.assertTrue(next(t for t in tasks if t['action'] == 'manually_send_reminder_day7')['due'])
        tasks = deadlines(p, '2026-10-01T00:00:00Z')
        self.assertEqual([t['action'] for t in tasks], ['review_no_response_cancel_and_full_refund'])
        self.assertEqual(p['state'], 'AWAITING_INTAKE')
        self.assertIsNone(p['approval'])

    def test_reply_clears_only_current_request_and_replacement_resets_clock(self):
        p = self.request()
        with self.assertRaises(ValueError):
            transition(p, ev('customer_replied', request_id='wrong'))
        with self.assertRaises(ValueError):
            transition(p, ev('input_requested', request_id='reset', request_kind='intake'))
        p = transition(p, ev('customer_replied', request_id='instructions'))
        self.assertEqual(deadlines(p), [])
        p = transition(p, ev('input_requested', '2026-09-22T00:00:00Z', request_id='clarify', request_kind='clarification'))
        self.assertEqual(deadlines(p)[0]['due_at'], '2026-09-24T00:00:00+00:00')

    def test_first_proof_uses_actual_usable_time_cannot_extend(self):
        p = transition(intake(), ev('route', gpx=GPX, source_verified=True))
        p = transition(p, ev('intake_usable', '2026-09-22T00:00:00Z',
                             usable_at='2026-09-21T05:00:00-05:00', complete_usable_verified=True))
        self.assertEqual(deadlines(p)[0]['due_at'], '2026-09-23T10:00:00+00:00')
        with self.assertRaises(ValueError):
            transition(p, ev('intake_usable', '2026-09-23T00:00:00Z',
                             usable_at='2026-09-22T00:00:00Z', complete_usable_verified=True))
        p = transition(p, ev('proof', '2026-09-22T00:00:00Z', version='v1', file=b'proof', layout_reviewed=True, color_confirmed=True))
        p = transition(p, ev('delivered', '2026-09-22T01:00:00Z', proof=p['proof'], recipient_verified=True, message_id='proof1'))
        self.assertNotIn('send_first_proof', [t['action'] for t in deadlines(p)])
        self.assertEqual(deadlines(p)[0]['due_at'], '2026-09-24T01:00:00+00:00')
        p = transition(p, ev('approve', '2026-09-22T02:00:00Z', proof=p['proof'], verified_key=p['key'], sender_verified=True, text='APPROVED FOR PRODUCTION'))
        self.assertEqual(deadlines(p), [])
        p = transition(p, ev('item_delivered', '2026-10-01T00:00:00Z'))
        self.assertEqual(deadlines(p)[0]['due_at'], '2026-10-15T00:00:00+00:00')

    def test_cancellation_retention_and_no_silent_production(self):
        p = self.request()
        with self.assertRaises(ValueError):
            transition(p, ev('cancelled_refunded'))
        p = transition(p, ev('cancelled_refunded', full_refund_verified=True))
        self.assertEqual(deadlines(p)[0]['due_at'], '2026-10-05T00:00:00+00:00')
        with self.assertRaises(ValueError):
            transition(p, ev('no_response'))
        with self.assertRaises(ValueError):
            transition(p, ev('files_deleted', checked_locations=['drive'], deletion_verified=True))
        p = transition(p, ev('files_deleted', checked_locations=['jotform', 'drive', 'local', 'working_files', 'proofs', 'backups'], deletion_verified=True))
        self.assertEqual(deadlines(p), [])

    def test_only_genuinely_new_proof_restarts_response_deadline(self):
        p = transition(intake(), ev('route', gpx=GPX, source_verified=True))
        p = transition(p, ev('proof', version='v1', file=b'proof1', layout_reviewed=True, color_confirmed=True))
        p = transition(p, ev('delivered', proof=p['proof'], recipient_verified=True, message_id='m1'))
        original = p['policy']['request'].copy()
        with self.assertRaises(ValueError):
            transition(p, ev('delivered', '2026-09-22T00:00:00Z', proof=p['proof'], recipient_verified=True, message_id='resend'))
        for version, content in [('v1', b'changed'), ('v2', b'proof1')]:
            with self.assertRaises(ValueError):
                transition(p, ev('proof', '2026-09-22T00:00:00Z', version=version, file=content, layout_reviewed=True, color_confirmed=True))
        self.assertEqual(p['policy']['request'], original)
        p = transition(p, ev('proof', '2026-09-22T00:00:00Z', version='v2', file=b'proof2', layout_reviewed=True, color_confirmed=True))
        p = transition(p, ev('delivered', '2026-09-22T01:00:00Z', proof=p['proof'], recipient_verified=True, message_id='m2'))
        self.assertEqual(p['policy']['request']['at'], '2026-09-22T01:00:00Z')
        self.assertEqual(p['policy']['first_proof_sent_at'], '2026-09-21T00:00:00Z')
        with self.assertRaises(ValueError):
            transition(p, ev('proof', '2026-09-22T02:00:00Z', version='v1', file=b'proof1', layout_reviewed=True, color_confirmed=True))

    def test_proof_cannot_overwrite_unanswered_intake_request(self):
        p = transition(intake(), ev('route', gpx=GPX, source_verified=True))
        p = transition(p, ev('input_requested', request_id='clarify', request_kind='clarification'))
        p = transition(p, ev('proof', version='v1', file=b'proof1', layout_reviewed=True, color_confirmed=True))
        with self.assertRaises(ValueError):
            transition(p, ev('delivered', proof=p['proof'], recipient_verified=True, message_id='m'))
        self.assertEqual(p['policy']['request']['id'], 'clarify')

    def test_deletion_completion_cannot_predate_closure(self):
        from tools.trace_deadlines import record_policy
        p = transition(self.request(), ev('cancelled_refunded', '2026-09-22T00:00:00Z', full_refund_verified=True))
        deletion = ev('files_deleted', checked_locations=['jotform', 'drive', 'local', 'working_files', 'proofs', 'backups'], deletion_verified=True)
        with self.assertRaises(ValueError):
            transition(p, deletion)
        with self.assertRaises(ValueError):
            record_policy(p, deletion)
        self.assertNotIn('deleted_at', p['policy'])

    def test_clock_validation_and_early_reminder(self):
        p = self.request()
        with self.assertRaises(ValueError):
            deadlines(p, '2026-09-21T00:00:00')
        with self.assertRaises(ValueError):
            transition(p, ev('customer_replied', '2026-09-20T00:00:00Z', request_id='instructions'))
        with self.assertRaises(ValueError):
            transition(p, ev('reminder_sent', request_id='instructions', stage='day7'))


if __name__ == '__main__':
    unittest.main()
