from app import app
from app import Events
import unittest
from unittest.mock import patch
import requests
from flask import json
from flask import jsonify
import mock

def get_random_id():
     all_events = []
     events = Events.query.all()
     for event in events:
          results = {
                    "id":event.id
          }
          all_events.append(results)
     import random
     random_id = random.choice(all_events)
     return random_id


class TestRoutes(unittest.TestCase):

        

        def setUp(self):
            self.app = app.test_client()
            self.app.testing = True
            self.client = app.test_client()
    
        def test_home(self):
            response = self.app.get('/')
            self.assertEqual(response.status_code, 200)
    
        def test_getevents(self):
            response = self.app.get('/events')
            self.assertEqual(response.status_code, 200)
    
        def test_geteventsgeojson(self):
            response = self.app.get('/events/geojson')
            self.assertEqual(response.status_code, 200)
    
        
        def test_create_event(self):
            response = self.app.post('/events', json = {"identifier":"lginwr","title":"test","location":4,"latitud":28.50,"longitud":-96.58})
            self.assertEqual(response.status_code, 200)

        # def test_create_event with id = 1
        def test_create_event_with_id_1(self):
            response = self.app.post('/events', json = {"id":1,"identifier":"lginwr","title":"test","location":4,"latitud":28.50,"longitud":-96.58})
            self.assertEqual(response.status_code, 200)

        def test_update_event(self):
            res = self.client.put('/events/5', json={
                "identifier": "lginwr2",
                "title": "test",
                "location": "6", 
                "latitud": 0.0,
                "longitud": 0.0
                })
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['response'], "Event Details updated")

            event = Events.query.filter(Events.identifier == 'lginwr2').first()
            self.assertTrue(event is not None)
            self.assertEqual(event.identifier, 'lginwr2')


        def test_delete_event(self):
            random_id = get_random_id()
            res = self.client.delete(f'/events/{random_id["id"]}')
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['response'], "Event Deleted")

            event = Events.query.filter(Events.identifier == 'lginwr2').first()
            self.assertTrue(event is not None)


