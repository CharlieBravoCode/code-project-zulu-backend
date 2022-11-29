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






#______________________ Other ______________________ #

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request"}), 400)


if __name__ == '__app__':
  app.run(debug=True)

#______________________ Routes ______________________ #

from routes import *