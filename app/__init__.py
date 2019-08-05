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

        @app.route('/creature', methods=['GET'])
        def all_creatures():
            creatures = [creature.to_dict() for creature in Creature.query.all()]

            return jsonify(creatures)

        @app.route('/creature/<int:id>', methods=['GET'])
        def one_creature(id):
            creature = Creature.query.get(id)

            return jsonify(creature.to_dict())

        @app.route('/creature', methods=['POST'])
        def create_creature():
            creature_info = request.json or request.form
            creature = Creature(name=creature_info.get('name'))
            db.session.add('creature')
            db.session.commit()

            return jsonify(creature.to_dict())

        @app.route('/creature/<int:id>', methods=['PUT'])
        def update_creature(id):
            creature_info = request.json or request.form

            creature_id = Creature.query.filter_by(id=id).update(creature_info)

            db.session.commit()
            return jsonify(creature_id)

        @app.route('/creature/<int:id>', methods=['DELETE'])
        def delete_creature(id):
            creature = Creature.query.get(id)
            db.session.delete(creature)
            db.session.commit()
            return jsonify(id)

        @app.route('/winged_creature', methods=['GET'])
        def all_winged_creatures():
            winged_creatures = [winged_creature.to_dict() for winged_creature in Winged_Creature.query.all()]

            return jsonify(winged_creatures)

        @app.route('/winged_creature/<int:id>', methods=['GET'])
        def one_winged_creature(id):
            winged_creature = Winged_Creature.query.get(id)

            return jsonify(winged_creature.to_dict())

        @app.route('/winged_creature', methods=['POST'])
        def create_winged_creature():
            winged_creature_info = request.json or request.form
            winged_creature = Winged_Creature(name=winged_creature_info.get('name'), creature_id=winged_creature_info.get('creature'))
            db.session.add('winged_creature')
            db.session.commit()

            return jsonify(winged_creature.to_dict())

        @app.route('/winged_creature/<int:id>', methods=['PUT'])
        def update_winged_creature(id):
            winged_creature_info = request.json or request.form

            winged_creature_id = Winged_Creature.query.filter_by(id=id).update(winged_creature_info)

            db.session.commit()
            return jsonify(winged_creature_id)

        @app.route('/winged_creature/<int:id>', methods=['DELETE'])
        def delete_winged_creature(id):
            winged_creature = Winged_Creature.query.get(id)
            db.session.delete(winged_creature)
            db.session.commit()
            return jsonify(id)

        @app.route("/creature/<int:id>/winged_creature")
        def get_winged_creature_in_creatures(id):
            winged_creature = [winged_creature.to_dict() for winged_creature in Creature.query.get(id).winged_creature]
            return jsonify(winged_creature)

            
    return app

from app.models import Creature, Winged_Creature