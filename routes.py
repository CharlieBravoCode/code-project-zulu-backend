from flask import Flask, jsonify, make_response,request, session, abort
from flask_login import UserMixin, login_user, LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from app import app, db
import os


db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))


#### Local Dev Postgres Docker ####

app.config['SECRET_KEY'] = 'mysecretkey'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@localhost:5432'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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


@cross_origin()  
@app.route("/bad-request")
def bad_request():
    return jsonify({"error": "Bad request"}), 400


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request"}), 400)