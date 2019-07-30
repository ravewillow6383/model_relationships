from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app(ConfigClass):

    app = Flask(__name__)
    
    app.config.from_object(ConfigClass)

    db.init_app(app)

    migrate.init_app(app, db)

    with app.app_context():

        @app.route('/creatures', methods=['GET'])
        def all_creatures():
            creatures = [creature.to_dict() for creature in Creature.query.all()]
            return jsonify(creatures)

        @app.route('/creatures/<int:id>')
        def one_creature(id):
            creature = Creature.query.get(id)
            return jsonify(creature.to_dict())

        @app.route('/creatures', method=['POST'])
        def create_creature():
            creature_info = request.json or request.form
            creature = Creature(name=creature_info.get('name'))
            db.session.add('creature')
            db.session.commit()

            return jsonify(creature.to_dict())

from app.models import Creature