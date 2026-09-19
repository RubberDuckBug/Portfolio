from flask_login import UserMixin
from app.database import db

class Candidate(UserMixin, db.Model):
    id = db.Coloumn(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, primary_key=False)
    password = db.Column(db.String(80), primary_key=False)