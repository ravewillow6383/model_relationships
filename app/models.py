from app import db

class Creature(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256), unique = True)
    winged_creature = db.relationship('Winged_Creature', backref='creature', lazy=True)

    def to_dict(self):
        return {
        'id':self.id, 
        'name':self.name,
        'winged_creature':[winged_creature.to_dict() for winged_creature in self.winged_creature] 
        }

class Winged_Creature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    creature_id = db.Column(db.Integer, db.ForeignKey('creature.id'), nullable=True)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}
