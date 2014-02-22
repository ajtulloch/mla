from app import db

class BatchTrainingRequest(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    trainingData = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            trainingData = self.trainingData,
            id = self.id
        )

    def __repr__(self):
        return '<BatchTrainingRequest %r>' % (self.id)
