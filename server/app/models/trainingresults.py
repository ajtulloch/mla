from app import db

class Trainingresults(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    dataset_id = db.Column(db.Integer, db.ForeignKey('dataset.id'))

    results = db.Column(db.String)

    def to_dict(self):
        return dict(
            results = self.results,
            dataset_id = self.dataset_id,
            id = self.id
        )

    def __repr__(self):
        return '<Trainingresults %r>' % (self.id)
