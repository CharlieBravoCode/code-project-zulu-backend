from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2
from flask_cors import CORS, cross_origin
#from flask_bcrypt import Bcrypt
#from flask_migrate import Migrate


from flask_login import (UserMixin, login_user, LoginManager, current_user, logout_user, login_required)



#______________________ Create App ______________________ #
app = Flask(__name__)
CORS(app)


#______________________ CORS ______________________ #

cors= CORS(app, resources={
    r"/*": {
        "origins": "https://code-project-zulu-cdc39ru51-charliebravocode.vercel.app"
        }
       }
    ) 


#______________________ Database Connection Config ______________________ #

#### Database in Heroku Setup ####

os.environ['DATABASE_URL'] = 'postgresql://iblhdktfqmapza:6a8b46b627797e8879823eccde4731f392eaf852ca37a742b1be3e8fe1c1c531@ec2-54-228-32-29.eu-west-1.compute.amazonaws.com:5432/dfeftmig21ojqf'

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

SQLAlchemy_DATABASE_URI = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = SQLAlchemy_DATABASE_URI

SECRET_KEY = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iblhdktfqmapza:6a8b46b627797e8879823eccde4731f392eaf852ca37a742b1be3e8fe1c1c531@ec2-54-228-32-29.eu-west-1.compute.amazonaws.com:5432/dfeftmig21ojqf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#### Database in Local Setup ####
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:seglniosi3ng9834ogno3ngkldowuez!$rmfmrRJjmelsmfdjUfnerurnfsegom490zj498t23nto(ugneukgbekgdj@localhost/zulu_db_postgres'


#______________________ User Login Set-Up ______________________ #
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

login_manager.init_app(app)
#db.init_app(app)
#Migrate.init_app(app, db)
#Bcrypt.init_app(app)



#______________________ Database Tables ______________________ #




#______________________ Routes ______________________ #





if __name__ == '__app__':
  app.run(debug=True)
