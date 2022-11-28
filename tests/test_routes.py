from app import app
from app import Events
import unittest
import json


class TestRoutes(unittest.TestCase):
    
        def setUp(self):
            self.app = app.test_client()
            self.app.testing = True
    
        def test_home(self):
            response = self.app.get('/')
            self.assertEqual(response.status_code, 200)
    
        def test_getevents(self):
            response = self.app.get('/events')
            self.assertEqual(response.status_code, 200)
    
        def test_geteventsgeojson(self):
            response = self.app.get('/events/geojson')
            self.assertEqual(response.status_code, 200)
    
        def test_update_event(self):
            response = self.app.put('/events/1')
            self.assertEqual(response.status_code, 200)
    
        def test_delete_event(self):
            response = self.app.delete('/events/1')
            self.assertEqual(response.status_code, 200)
    
        def test_create_event(self):
            response = self.app.post('/events')
            self.assertEqual(response.status_code, 200)
    
        def test_get_event(self):
            response = self.app.get('/events/1')
            self.assertEqual(response.status_code, 200)
    
        def test_get_event_geojson(self):
            response = self.app.get('/events/1/geojson')
            self.assertEqual(response.status_code, 200)
        
