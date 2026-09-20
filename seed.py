from app import create_website
from app.database import db
from app.models import Employer, Candidate
from werkzeug.security import generate_password_hash

app = create_website()

with app.app_context():
    db.create_all()
    if not Employer.query.filter_by(username="AdamSmasher").first():
        user = Employer(username="AdamSmasher", password=generate_password_hash("password"))
        db.session.add(user)
        db.session.commit()
        print("Test user created.")
    else:
        print("User already exists.")