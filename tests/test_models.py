import unittest
from app import Events


class TestEvents(unittest.TestCase):
    def setUp(self): 
        self.event = Events(id=1, identifier="id1", title="My Event", location="NYC", latitud=40.7128, longitud=74.0060)

    def test_title(self):
        self.assertEqual(self.event.title, "My Event")

    def test_location(self):
        self.assertEqual(self.event.location, "NYC")

    def test_latitud_and_longitud(self):
        self.assertEqual(self.event.latitud, 40.7128)
        self.assertEqual(self.event.longitud, 74.0060)