from app import db

class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    name = db.Column(db.String, unique = True)
    
    examples = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            name = self.name,
            examples = self.examples,
            id = self.id
        )

    def __repr__(self):
        return '<Dataset %r>' % (self.id)
