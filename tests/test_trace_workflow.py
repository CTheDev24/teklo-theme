import unittest
from tools.trace_workflow import new_piece, transition, validate_gpx
GPX=b'<gpx><trk><trkseg><trkpt lat="1" lon="2"/><trkpt lat="1.01" lon="2.01"/></trkseg></trk></gpx>'
DATA=dict(runner='A'*250,race='Test',date='2026-01-01',location='Synthetic',distance='10K',finish='Nocturne',accent='Match My Medal Color',route_method='gpx',omit_finish_time=True)
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
        p=transition(p,event('no_response'));self.assertEqual(p['state'],'AWAITING_APPROVAL')
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
            self.assertEqual(p['state'],'NEEDS_INPUT');self.assertIsNone(p['approval'])
    def test_unit_range(self):
        with self.assertRaises(ValueError):new_piece('s','o','l',3,2)
if __name__=='__main__':unittest.main()
