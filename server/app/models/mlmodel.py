from app import db

class Mlmodel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    name = db.Column(db.String)
    
    serialized = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            name = self.name,
            serialized = self.serialized,
            id = self.id
0        )

    def __repr__(self):
        return '<Mlmodel %r>' % (self.id)
