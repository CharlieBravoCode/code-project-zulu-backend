from flask import Flask, jsonify,request, session

from flask_sqlalchemy import SQLAlchemy

import psycopg2
import os



#______________________  App ______________________ #

app = Flask(__name__)
CORS(app)
app.secret_key = 'ewilgfnoguoe4nrkvnjsnielngoigo4gnnvoilIWFUWBGW93giownglesngjln3ljn3oin((nifneifnldkne'

#______________________ CORS ______________________ #

cors= CORS(app, resources={
    r"/*": {
        "origins": "https://code-project-zulu-cdc39ru51-charliebravocode.vercel.app"
        }
       }
    ) 

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

#### Database Local ####
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:seglniosi3ng9834ogno3ngkldowuez!$rmfmrRJjmelsmfdjUfnerurnfsegom490zj498t23nto(ugneukgbekgdj@localhost/zulu_db_postgres'



@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


if __name__ == '__app__':
  app.run(debug=True)
  
