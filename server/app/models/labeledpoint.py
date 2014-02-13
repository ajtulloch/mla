from app import db

class Labeledpoint(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    label = db.Column(db.Boolean)
    
    features = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            label = self.label,
            features = self.features,
            id = self.id
        )

    def __repr__(self):
        return '<Labeledpoint %r>' % (self.id)
