from flask import Flask, jsonify, make_response,request, session, abort
from flask_login import UserMixin, login_user, LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os
from cors import setup_cors




#______________________  App ______________________ #


app = Flask(__name__)
CORS(app)
# app.secret_key = 'ewilgfnoguoe4nrkvnjsnielngoigo4gnnvoilIWFUWBGW93giownglesngjln3ljn3oin((nifneifnldkne'
setup_cors(app)



#______________________ Database Connection Config ______________________ #

db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))

#### Local Dev Postgres Docker ####


app.config['SECRET_KEY'] = 'mysecretkey'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@localhost:5432'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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


#______________________ User Login Set-Up ______________________ #

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"
login_manager.init_app(app)


#______________________ Database Tables ______________________ #

class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key = True)
    identifier = db.Column(db.String)
    title = db.Column(db.String)
    location = db.Column(db.Integer())
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)

    def __repr__(self):
        return "<Event %r>" % self.title 


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255))
    #active = db.Column(db.Boolean)

    def __repr__(self):
        return '<User %r>' % self.username
    
    def get_id(self):
            return str(self.id)


#______________________ Routes ______________________ #

#____________Routes - Content_______________ #

@cross_origin()
# @login_required
@app.route('/events', methods = ['POST'])
# @requires_auth
def create_event():
    event_data = request.json

    identifier = event_data['identifier']
    title  = event_data['title']
    location = event_data['location']
    latitud = event_data['latitud']
    longitud = event_data['longitud']
  
    event = Events(identifier = identifier, title = title, location = location, latitud = latitud, longitud = longitud)
    db.session.add(event)
    db.session.commit()    

    return jsonify({"success": True,"response":"Event added"})


@cross_origin()  
@app.route("/")
# @requires_auth
def home():
    return "Hello World!"


@cross_origin()    
@app.route('/events', methods = ['GET'])
# @requires_auth
def getevents():
     all_events = []
     events = Events.query.all()
     for event in events:
          results = {
                    "id":event.id,
                    "identifier":event.identifier,
                    "title":event.title,
                    "location":event.location,
                    "latitud":event.latitud,
                    "longitud":event.longitud
          }
          all_events.append(results)

     return jsonify(all_events)


@cross_origin() 
@app.route('/events/geojson', methods = ['GET'])
# @requires_auth
def geteventsgeojson():
        points = []
        events = Events.query.all()
        for event in events:
            points.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [event.longitud, event.latitud]
                },
                "properties": {
                    "title": event.title,
                    "identifier": event.identifier,
                    "location": event.location,
                    "id": event.id
                }
            })
        return jsonify({"type": "FeatureCollection", "features": points})



@cross_origin()  
@app.route("/events/<int:event_id>", methods = ["PUT"])
# @requires_auth
def update_event(event_id):
    event = Events.query.get(event_id)
    identifier = request.json['identifier']
    title = request.json['title']
    location = request.json['location']
    latitud = request.json['latitud']
    longitud = request.json['longitud']

    if event is None:
        abort(404)
    else:
        event.identifier = identifier
        event.title = title
        event.location = location
        event.latitud = latitud
        event.longitud = longitud
        db.session.add(event)
        db.session.commit()
        return jsonify({"success": True, "response": "Event Details updated"})



@cross_origin()  
@app.route("/events/<int:event_id>", methods = ["DELETE"])
# @requires_auth
def delete_event(event_id):
    event = Events.query.get(event_id)

    if event is None:
        abort(404)
    else:
        db.session.delete(event)
        db.session.commit()
        return jsonify({"success": True, "response": "Event Deleted"})

# Add the URL '/bad-request' so that it can be handled by the errorhandler.
@cross_origin()  
@app.route("/bad-request")
def bad_request():
    return jsonify({"error": "Bad request"}), 400



#____________Routes - User Login_______________ #
### Not yet fully implemented - currently auth0 in use###

@login_manager.user_loader
def load_user(id):
    try:
        return User.query.get(int(id))
    except:
        return None


def login_user():
    return current_user.is_authenticated


@cross_origin()
@app.route('/auth/login', methods=['POST'])
def login():
    session.pop('id', None)
    
    user_data = request.json
    username = user_data['username']
    password = user_data['password']

    #user = User.query.filter_by(username = username).first()
    user = db.session.query(User).filter_by(username=username).first()
    print(f'This is user: {user}')
    print(f'This is user.username: {user.username}')
    print(f'This is user.password: {user.password}')

    if user is not None and user.username == username and user.password == password:
        login_user()
        session['id'] = user.id

    # return a response with the a cookie and the user's id
        resp = make_response(jsonify({'message': 'Logged in successfully'}))
        resp.set_cookie('user_id', value=str(user.id), domain=".code-project-zulu.vercel.app")
        print(f'This is the cookie: {resp}')
        return resp
    else:
        return jsonify({'error': 'Invalid username or password'})


#____________Other_______________ #

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request"}), 400)


if __name__ == '__app__':
  app.run(debug=True)
  
