from flask import Flask
from app.config import Config
from app.database import db
from flask_login import LoginManager

# https://flask-login.readthedocs.io/en/latest/#flask-login
login_manager = LoginManager()

# Using a function so it creates an instance of the Flask app which can be used for real, tests ... with a changed set of configs
def create_website():
    # Creates the Flask instance
    app = Flask(__name__)
    # Loads in the config file (secret key)
    app.config.from_object(Config)

    # Connects the database to the Flask instance
    db.init_app(app)

    login_manager.init_app(app)
    # Redirects to index.html if user not logged in
    login_manager.login_view = 'auth.login'

    # Collects all the routes
    from app.routes import main
    from app.auth import auth
    # Adds them to the instance
    app.register_blueprint(main)
    app.register_blueprint(auth)

    with app.app_content():
        db.create_all()

    return app

from app.models import Candidate

@login_manager.user_loader
def load_user(username):
    # Replace body when have database
    return Candidate(username, password)