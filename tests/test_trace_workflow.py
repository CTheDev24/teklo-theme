import unittest
from tools.trace_workflow import new_piece, transition, validate_gpx
GPX=b'<gpx><trk><trkseg><trkpt lat="1" lon="2"/><trkpt lat="1.01" lon="2.01"/></trkseg></trk></gpx>'
DATA=dict(runner='A'*250,race='Test',date='2026-01-01',location='Synthetic',distance='10K',finish='Nocturne',accent='Match My Medal Color',route_method='gpx',omit_finish_time=True,route_source='synthetic-route',activity_url='https://example.invalid/activity',course_name='Test',course_year='2026',course_distance='10K',course_location='Synthetic')
def event(kind,**kw):return dict(type=kind,at='2026-09-21T00:00:00Z',evidence='synthetic-test',**kw)
def intake(unit=1,method='gpx'):
    p=new_piece('test-shop','test-order','test-line',unit,2)
    return transition(p,event('intake',verified_key=p['key'],data={**DATA,'route_method':method}))
class Workflow(unittest.TestCase):
    def test_all_sources_need_verified_route(self):
        for method in ('gpx','activity','course','map'):
            p=intake(method=method)
            with self.assertRaises(ValueError):transition(p,event('route',gpx=GPX))
            p=transition(p,event('route',gpx=GPX,source_verified=True))
            self.assertEqual(p['state'],'AWAITING_PROOF')
    def test_invalid_gpx(self):
        for data in (b'bad',b'<gpx/>',b'<gpx><trkpt lat="nan" lon="1"/></gpx>',b'<!DOCTYPE gpx><gpx/>'):
            with self.assertRaises(Exception):validate_gpx(data)
    def test_two_pieces_approval_and_revision(self):
        p=intake();other=intake(2)
        p=transition(p,event('route',gpx=GPX,source_verified=True))
        p=transition(p,event('proof',version='1',file=b'proof',layout_reviewed=True,color_confirmed=True))
        with self.assertRaises(ValueError):transition(p,event('approve',proof=p['proof'],verified_key=p['key'],sender_verified=True,text='APPROVED FOR PRODUCTION'))
        p=transition(p,event('delivered',proof=p['proof'],recipient_verified=True,message_id='synthetic'))
        p=transition(p,event('no_response'));self.assertEqual(p['state'],'HOLD_NO_RESPONSE')
        p=transition(p,event('resume'))
        with self.assertRaises(ValueError):transition(p,event('approve',proof=p['proof'],verified_key=other['key'],sender_verified=True,text='APPROVED FOR PRODUCTION'))
        p=transition(p,event('approve',proof=p['proof'],verified_key=p['key'],sender_verified=True,text='APPROVED FOR PRODUCTION'))
        self.assertEqual(p['state'],'APPROVED');self.assertEqual(other['state'],'AWAITING_ROUTE')
        p=transition(p,event('route',gpx=GPX,source_verified=True));self.assertIsNone(p['approval'])
    def test_missing_time_and_identity(self):
        p=new_piece('s','o','l',1,1)
        with self.assertRaises(ValueError):transition(p,event('intake',verified_key=['wrong'],data=DATA))
        p=transition(p,event('intake',verified_key=p['key'],data={**DATA,'omit_finish_time':False}))
        self.assertEqual(p['state'],'NEEDS_INPUT')
    def test_edge_cases_hold(self):
        for kind in ('invalid_input','private_link','unavailable_course','color_unclear'):
            p=transition(intake(),event(kind));p=transition(p,event('no_response'))
            self.assertEqual(p['state'],'HOLD_NO_RESPONSE');self.assertIsNone(p['approval'])
    def test_unit_range(self):
        with self.assertRaises(ValueError):new_piece('s','o','l',3,2)

class Persistence(unittest.TestCase):
    def setUp(self):
        import tempfile
        from pathlib import Path
        from tools.trace_operations import Ledger
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.ledger = Ledger(self.root / 'ledger')
        self.identifier = self.ledger.create('s', 'o', 'l', 1, 2)

    def test_persistence_duplicate_retry_and_revision_conflict(self):
        from tools.trace_operations import Ledger
        e = event('intake', id='intake-1', verified_key=['s', 'o', 'l', 1], data=DATA)
        first = self.ledger.apply(self.identifier, e, 0)
        restored = Ledger(self.root / 'ledger')
        self.assertEqual(first, restored.read(self.identifier))
        self.assertEqual(first, restored.apply(self.identifier, e, 0))
        with self.assertRaises(ValueError):
            restored.apply(self.identifier, {**e, 'id': 'different-event'}, 0)
        with self.assertRaises(ValueError):
            restored.apply(self.identifier, {**e, 'evidence': 'changed'}, 1)
        self.assertEqual(first, restored.read(self.identifier))

    def test_artifact_hash_and_no_partial_write_on_invalid_input(self):
        self.ledger.apply(self.identifier, event('intake', id='i', verified_key=['s','o','l',1], data=DATA), 0)
        route = self.root / 'route.gpx'
        route.write_bytes(b'not XML')
        with self.assertRaises(ValueError):
            self.ledger.apply(self.identifier, event('route', id='r', gpx_file=str(route), source_verified=True), 1)
        self.assertEqual(self.ledger.read(self.identifier)['piece']['revision'], 1)
        route.write_bytes(GPX)
        accepted = self.ledger.apply(self.identifier, event('route', id='r', gpx_file=str(route), source_verified=True), 1)
        self.assertEqual(accepted['piece']['route']['sha256'], validate_gpx(GPX)['sha256'])
        self.assertNotIn('gpx_file', accepted['receipts'][-1]['event'])

    def test_lock_and_duplicate_creation(self):
        with self.assertRaises(ValueError):
            self.ledger.create('s','o','l',1,2)
        lock = self.ledger.path(self.identifier).with_suffix('.lock')
        lock.touch()
        with self.assertRaises(ValueError):
            self.ledger.apply(self.identifier, event('no_response', id='n'), 0)
        self.assertEqual(self.ledger.read(self.identifier)['piece']['revision'], 0)

    def test_private_storage_and_path_traversal(self):
        from tools.trace_operations import Ledger
        repo = self.root / 'checkout'
        repo.mkdir()
        (repo / '.git').touch()
        with self.assertRaises(ValueError):
            Ledger(repo / 'orders')
        with self.assertRaises(ValueError):
            self.ledger.read('../outside')


class AdditionalGates(unittest.TestCase):
    def proof(self):
        p = transition(intake(), event('route',gpx=GPX,source_verified=True))
        return transition(p,event('proof',version='v1',file=b'proof1',layout_reviewed=True,color_confirmed=True))

    def test_malformed_coordinates_and_encoding(self):
        for gpx in (b'<gpx><trkpt lat="1"/></gpx>', b'<gpx><trkpt lat="91" lon="0"/></gpx>',
                    b'<gpx><trkpt lat="1" lon="inf"/></gpx>', b'<gpx><trkpt lat="1" lon="1"/><trkpt lat="1" lon="1"/></gpx>',
                    '<!DOCTYPE gpx><gpx/>'.encode('utf-16')):
            with self.assertRaises(ValueError):
                validate_gpx(gpx)

    def test_missing_alternative_and_nullable_required_fields(self):
        p = new_piece('s','o','l',1,1)
        for data in ({**DATA, 'runner':None}, {**DATA, 'route_source':''},
                     {**DATA, 'route_method':'activity', 'activity_url':'javascript:bad'},
                     {**DATA, 'route_method':'course', 'course_year':''}):
            incomplete = transition(p,event('intake',verified_key=p['key'],data=data))
            self.assertEqual(incomplete['state'],'NEEDS_INPUT')
            with self.assertRaises(ValueError):
                transition(incomplete,event('route',gpx=GPX,source_verified=True))

    def test_stale_proof_and_nonresponse_hold(self):
        p = self.proof()
        old_proof = p['proof']
        p = transition(p,event('proof',version='v2',file=b'proof2',layout_reviewed=True,color_confirmed=True))
        with self.assertRaises(ValueError):
            transition(p,event('delivered',proof=old_proof,recipient_verified=True,message_id='m'))
        p = transition(p,event('delivered',proof=p['proof'],recipient_verified=True,message_id='m'))
        p = transition(p,event('no_response'))
        with self.assertRaises(ValueError):
            transition(p,event('approve',proof=p['proof'],verified_key=p['key'],sender_verified=True,text='APPROVED FOR PRODUCTION'))
        p = transition(p,event('resume'))
        p = transition(p,event('approve',proof=p['proof'],verified_key=p['key'],sender_verified=True,text='APPROVED FOR PRODUCTION'))
        p = transition(p,event('correction'))
        self.assertEqual(p['state'],'NEEDS_INPUT')
        self.assertIsNone(p['approval'])
        with self.assertRaises(ValueError):
            transition(p,event('proof',version='v3',file=b'proof3',layout_reviewed=True,color_confirmed=True))

class Cli(unittest.TestCase):
    def test_cli_init_queue_and_two_piece_isolation(self):
        from contextlib import redirect_stdout
        from io import StringIO
        import json
        import tempfile
        from tools.trace_operations import main, Ledger
        with tempfile.TemporaryDirectory() as root:
            for unit in (1,2):
                output = StringIO()
                with redirect_stdout(output):
                    self.assertEqual(main(['--root',root,'init','--shop','s','--order','o','--line','l','--unit',str(unit),'--quantity','2']),0)
                identifier = json.loads(output.getvalue())['piece_id']
                self.assertEqual(Ledger(root).read(identifier)['piece']['key'][-1],unit)
            output = StringIO()
            with redirect_stdout(output):
                self.assertEqual(main(['--root',root,'queue']),0)
            self.assertEqual(len(json.loads(output.getvalue())),2)

if __name__ == '__main__':
    unittest.main()
