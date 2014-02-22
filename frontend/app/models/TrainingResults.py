from app import db

class TrainingResults(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    jsonString = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            jsonString = self.jsonString,
            id = self.id
        )

    def __repr__(self):
        return '<TrainingResults %r>' % (self.id)
