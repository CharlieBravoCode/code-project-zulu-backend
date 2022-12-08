from flask import Flask, jsonify
from flask_cors import CORS, cross_origin




def setup_cors(app):
  cors= CORS(app, resources={
      r"/*": {
          "origins": "https://code-project-zulu-cdc39ru51-charliebravocode.vercel.app"
          }
         }
      ) 