import pytest
from app import create_app, db
from config import Config
from app.models import Creature, Winged_Creature

class testConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'sqlite://'



