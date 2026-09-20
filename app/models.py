from flask_login import UserMixin
from app.database import db

class Employer(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, primary_key=False, nullable=False)
    password = db.Column(db.String(200), primary_key=False, nullable=False)

    # Overridden default method from UserMixin
    def get_id(self):
        return f"Employer-{self.id}"

class Candidate(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, primary_key=False, nullable=False)
    password = db.Column(db.String(200), primary_key=False, nullable=False)

    def get_id(self):
        return f"Candidate-{self.id}"