import unittest
import json
from app import app


class TestErrorHandler(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # write a test for a 400 error
    def test_bad_request(self):
        response = self.app.get('/bad-request')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Bad request')