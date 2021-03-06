from flask import Flask
from .models import db


def create_app():
    flask_app = Flask(__name__)
    # change <name> and <host> below according to your own
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:<name>@<host>/' 
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    return flask_app