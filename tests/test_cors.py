import unittest
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)

class TestCors(unittest.TestCase):
    def test_cors(self):
        self.assertIsNotNone(CORS(app))
