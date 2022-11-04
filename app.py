from flask import Flask, jsonify,request, session
from flask_sqlalchemy import SQLAlchemy



import psycopg2
import os


app = Flask(__name__)




#______________________ Database Connection Config ______________________ #

db = SQLAlchemy(app)

#### Database in Heroku  ####

os.environ['DATABASE_URL'] = 'postgresql://iblhdktfqmapza:6a8b46b627797e8879823eccde4731f392eaf852ca37a742b1be3e8fe1c1c531@ec2-54-228-32-29.eu-west-1.compute.amazonaws.com:5432/dfeftmig21ojqf'

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

SQLAlchemy_DATABASE_URI = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = SQLAlchemy_DATABASE_URI

SECRET_KEY = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iblhdktfqmapza:6a8b46b627797e8879823eccde4731f392eaf852ca37a742b1be3e8fe1c1c531@ec2-54-228-32-29.eu-west-1.compute.amazonaws.com:5432/dfeftmig21ojqf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




if __name__ == '__app__':
  app.run(debug=True)
  
