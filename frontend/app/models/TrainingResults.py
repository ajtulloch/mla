from app import db
import json


class TrainingResults(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    jsonReport = db.Column(db.String)

    def to_dict(self):
        return dict(
            jsonReport = json.loads(self.jsonReport),
            id = self.id
        )

    def __repr__(self):
        return '<TrainingResults %r>' % (self.id)
