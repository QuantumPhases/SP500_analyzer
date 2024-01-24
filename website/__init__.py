from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_REQUESTS = "SP500_Database.db"

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ("Veldin321")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SP500_Database.db'
    db.init_app(app)

    from .views import views
    from .model import SP500_Realtime_Data

    create_database(app)

    app.register_blueprint(views, url_prefix="/")

    return app

from . import db

def create_database(app):
    with app.app_context():
        db.create_all()