from flask_sqlalchemy import SQLAlchemy
from app import app
import os

def configure_db():
    #### Local Dev Postgres Docker ####
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@localhost:5432'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    #### Database in Heroku  ####
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iblhdktfqmapza:6a8b46b627797e8879823eccde4731f392eaf852ca37a742b1be3e8fe1c1c531@ec2-54-228-32-29.eu-west-1.compute.amazonaws.com:5432/dfeftm