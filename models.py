from app import db
from flask_login import UserMixin

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
