from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from app import db, app
from models import User, Events
from flask_login import login_manager



#____________Routes - User Login_______________ #

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@cross_origin()
@app.route('/login', methods=['POST'])
def login():
    user_data = request.json

    username = user_data['username']
    password = user_data['password']

    user = User.query.filter_by(username=username).first()

    if user.username == username and user.password == password:
        login_user(user)
        return jsonify({'username': user.username})





#____________Routes - Content_______________ #


@cross_origin()
@app.route('/events', methods = ['POST'])
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
def home():
    return "Hello World!"

@cross_origin()    
@app.route('/events', methods = ['GET'])
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
def delete_event(event_id):
    event = Events.query.get(event_id)

    if event is None:
        abort(404)
    else:
        db.session.delete(event)
        db.session.commit()
        return jsonify({"success": True, "response": "Event Deleted"})

