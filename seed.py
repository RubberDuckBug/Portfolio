from app import create_website
from app.database import db
from app.models import Candidate
from werkzeug.security import generate_password_hash

app = create_website()

with app.app_context():
    db.create_all()
    if not Candidate.query.filter_by(username="AdamSmasher").first():
        user = Candidate(username="AdamSmasher", password_hash=generate_password_hash("password"))
        db.session.add(user)
        db.session.commit()
        print("Test user created.")
    else:
        print("User already exists.")