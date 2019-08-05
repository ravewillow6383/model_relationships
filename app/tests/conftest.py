import pytest
from app import create_app, db
from config import Config
from app.models import Creature, Winged_Creature

class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'sqlite://'


@pytest.fixture()
def client():

    app = create_app(TestConfig)

    app_context = app.app_context()

    app_context.push()

    db.create_all()

    with app.test_client() as client:
        yield client

    db.session.remove()

    db.drop_all()

    app_context.pop()


@pytest.fixture()
def sample_creature(client):
    creature = Creature(name='Birds')
    db.session.add(creature)
    db.session.commit()
    return creature

@pytest.fixture()
def sample_winged_creature(sample_creature):
    winged_creature = Winged_Creature(name='Flightless cormorant', creature=sample_creature)
    db.session.add(winged_creature)
    db.session.commit()
    return winged_creature

@pytest.fixture()
def lone_winged_creature(client):
    winged_creature = Winged_Creature(name='Zburator')
    db.session.add(winged_creature)
    db.session.commit()
    return winged_creature






