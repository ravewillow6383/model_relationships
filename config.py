from flask_sqlalchemy import SQLAlchemy
from app import create_app

class Config(object):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    db = SQLAlchemy(app)


    SQLALCHEMY_TRACK_MODIFICATIONS = False
