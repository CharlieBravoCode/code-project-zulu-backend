from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from cors import setup_cors
import os


app = Flask(__name__)
CORS(app)
setup_cors(app)

#______________________ Database Connection Config ______________________ #

db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))

#### Local Dev Postgres Docker ####

app.config['SECRET_KEY'] = 'mysecretkey'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@localhost:5432'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#### Database in Heroku  ####

# os.environ['DATABASE_URL'] = 'postgresql://iblhdktfqmapza:6a8b46b627797e8879823eccde4731f392eaf852ca37a742b1be3e8fe1c1c531@ec2-54-228-32-29.eu-west-1.compute.amazonaws.com:5432/dfeftmig21ojqf'

# DATABASE_URL = os.environ['DATABASE_URL']
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# SQLAlchemy_DATABASE_URI = os.environ['DATABASE_URL']
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLAlchemy_DATABASE_URI

# SECRET_KEY = os.environ.get('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iblhdktfqmapza:6a8b46b627797e8879823eccde4731f392eaf852ca37a742b1be3e8fe1c1c531@ec2-54-228-32-29.eu-west-1.compute.amazonaws.com:5432/dfeftmig21ojqf'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#### Database Local ####
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:seglniosi3ng9834ogno3ngkldowuez!$rmfmrRJjmelsmfdjUfnerurnfsegom490zj498t23nto(ugneukgbekgdj@localhost/zulu_db_postgres'




#______________________ Other ______________________ #

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request"}), 400)


if __name__ == '__app__':
  app.run(debug=True)

#______________________ Routes ______________________ #

from routes import *