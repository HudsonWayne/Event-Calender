from . import db
from datetime import datetime

class Event (db.Model):
    id = db.Column(db.Integer, primary_key=True)