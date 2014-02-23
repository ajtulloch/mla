from app import app, db
from app.models import TrainingResults
from flask import abort, jsonify, request
import json


@app.route('/app/Trainingresults', methods=['GET'])
def get_all_Trainingresults():
    entities = TrainingResults.TrainingResults.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/app/Trainingresults/<int:id>', methods = ['GET'])
def get_TrainingResults(id):
    entity = TrainingResults.TrainingResults.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/app/Trainingresults', methods = ['POST'])
def create_TrainingResults():
    entity = TrainingResults.TrainingResults(
        jsonString = request.json['jsonString']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/app/Trainingresults/<int:id>', methods = ['PUT'])
def update_TrainingResults(id):
    entity = TrainingResults.TrainingResults.query.get(id)
    if not entity:
        abort(404)
    entity = TrainingResults.TrainingResults(
        jsonString = request.json['jsonString'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/app/Trainingresults/<int:id>', methods = ['DELETE'])
def delete_TrainingResults(id):
    entity = TrainingResults.TrainingResults.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 200
