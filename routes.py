import logging
from flask import jsonify, make_response,request, abort
from flask_cors import cross_origin
from app import app, db
from db import configure_db


configure_db()


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
@app.route("/")
def home():
    return "Hello World!"


@cross_origin()
@app.route('/events', methods = ['POST'])
def create_event():
    try:
      event_data = request.json

      identifier = event_data['identifier']
      title  = event_data['title']
      location = event_data['location']
      latitud = event_data['latitud']
      longitud = event_data['longitud']
  
      event = Events(identifier = identifier, title = title, location = location, latitud = latitud, longitud = longitud)
      db.session.add(event)
      db.session.commit()    

      logging.info("Event added")
      return jsonify({"success": True,"response":"Event added"})
    except Exception as e:
      logging.error("Error adding event: " + str(e))
      return make_response(jsonify({"error": "Error adding event"}), 400)


@cross_origin()    
@app.route('/events', methods = ['GET'])
def getevents():
    try:
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
    except Exception as e:
      logging.error("Error getting events: " + str(e))
      return make_response(jsonify({"error": "Error getting events"}), 400)


@cross_origin() 
@app.route('/events/geojson', methods = ['GET'])
def geteventsgeojson():
    try:
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
    except Exception as e:
      logging.error("Error getting events geojson: " + str(e))
      return make_response(jsonify({"error": "Error getting events geojson"}), 400)


@cross_origin()  
@app.route("/events/<int:event_id>", methods = ["PUT"])
def update_event(event_id):
    try:
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
        logging.info("Event updated")
        return jsonify({"success": True, "response": "Event Details updated"})
    except Exception as e:
      logging.error("Error updating event: " + str(e))
      return make_response(jsonify({"error": "Error updating event"}), 400)


@cross_origin()  
@app.route("/events/<int:event_id>", methods = ["DELETE"])
def delete_event(event_id):
    try:
      event = Events.query.get(event_id)

      if event is None:
        abort(404)
      else:
        db.session.delete(event)
        db.session.commit()
        logging.info("Event deleted")
        return jsonify({"success": True, "response": "Event Deleted"})
    except Exception as e:
      logging.error("Error deleting event: " + str(e))
      return make_response(jsonify({"error": "Error deleting event"}), 400)


@cross_origin()  
@app.route("/bad-request")
def bad_request():
    return jsonify({"error": "Bad request"}), 400


def error_handler(error):
    return make_response(jsonify({"error": error.description}), error.code)

@app.errorhandler(400)
@app.errorhandler(404)
def handle_error(error):
    return error_handler(error)