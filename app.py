from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from cors import setup_cors


app = Flask(__name__)
CORS(app)
setup_cors(app)
db = SQLAlchemy(app)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request"}), 400)


if __name__ == '__app__':
  app.run(debug=True)


from routes import *