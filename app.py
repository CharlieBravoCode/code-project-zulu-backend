from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cors import setup_cors


app = Flask(__name__)
db = SQLAlchemy(app)
setup_cors(app)


if __name__ == '__app__':
  app.run(debug=True)


from routes import *