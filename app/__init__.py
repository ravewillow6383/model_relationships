from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from dotenv import load_dotenv

# load_dotenv()

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

        @app.route('/creatures/<int:id>', methods=['GET'])
        def one_creature(id):
            creature = Creature.query.get(id)

            return jsonify(creature.to_dict())

        @app.route('/creatures', methods=['POST'])
        def create_creature():
            creature_info = request.json or request.form
            creature = Creature(name=creature_info.get('name'))
            db.session.add('creature')
            db.session.commit()

            return jsonify(creature.to_dict())

        @app.route('/creatures/<int:id>', methods=['PUT'])
        def update_creature(id):
            creature_info = request.json or request.form

            creature_id = Creature.query.filter_by(id=id).update(creature_info)

            db.session.commit()
            return jsonify(creature_id)

        @app.route('/creatures/<int:id>', methods=['DELETE'])
        def delete_creature(id):
            creature = Creature.query.get(id)
            db.session.delete(creature)
            db.session.commit()
            return jsonify(id)
            
    return app

from app.models import Creature