# from app import db

# class Creature(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(256), unique = True)
#     winged_creature = db.relationship('Winged_Creature', backref='creature', lazy=True)

#     def to_dict(self):
#         return {'id':self.id, 'name':self.name }
