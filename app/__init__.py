from flask import Flask
from app.config import Config

# Using a function so it creates an instance of the Flask app which can be used for real, tests ... with a changed set of configs
def create_website():
    # Creates the Flask instance
    app = Flask(__name__)
    # Loads in the config file (secret key)
    app.config.from_object(Config)

    # Collects all the routes
    from app.routes import main
    # Adds them to the instance
    app.register_blueprint(main)

    return app