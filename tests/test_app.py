import unittest
from flask import Flask


class TestFlask(unittest.TestCase):
    def test_flask(self):
        app = Flask(__name__)
        self.assertIsInstance(app, Flask)