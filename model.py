from app import db

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