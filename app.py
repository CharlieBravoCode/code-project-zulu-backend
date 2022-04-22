from flask import Flask, jsonify,request, abort
from flask_sqlalchemy import SQLAlchemy
#from flask_cors import CORS, cross_origin


app = Flask(__name__)
#CORS(app)

#### Database in Local Setup ####
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:seglniosi3ng9834ogno3ngkldowuez!$rmfmrRJjmelsmfdjUfnerurnfsegom490zj498t23nto(ugneukgbekgdj@localhost/zulu_db_postgres'

#### Database in Heroku Setup ####
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kmsrexvzdwejei:a375072228ebc01633018d08896273d133f1178f2b5eed57705a5f19e562a39f@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/dahqvr1vpumlpc'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == '__app__':
  app.run(debug=True)


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


#@cross_origin()
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



@app.route("/")
def home():
    return "Hello World!"

#@cross_origin()    
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


#@cross_origin() 
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



#@cross_origin()  
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


#@cross_origin()  
@app.route("/events/<int:event_id>", methods = ["DELETE"])
def delete_event(event_id):
    event = Events.query.get(event_id)

    if event is None:
        abort(404)
    else:
        db.session.delete(event)
        db.session.commit()
        return jsonify({"success": True, "response": "Event Deleted"})




