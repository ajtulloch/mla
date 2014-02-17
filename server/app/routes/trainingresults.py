from app import app, db
from app.models import trainingresults
from flask import abort, jsonify, request
import datetime
import json

@app.route('/mlserver/trainingresults', methods = ['GET'])
def get_all_trainingresults():
    entities = trainingresults.Trainingresults.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/mlserver/trainingresults/<int:id>', methods = ['GET'])
def get_trainingresults(id):
    entity = trainingresults.Trainingresults.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/mlserver/trainingresults', methods = ['POST'])
def create_trainingresults():
    entity = trainingresults.Trainingresults(
        results = request.json['results']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/mlserver/trainingresults/<int:id>', methods = ['PUT'])
def update_trainingresults(id):
    entity = trainingresults.Trainingresults.query.get(id)
    if not entity:
        abort(404)
    entity = trainingresults.Trainingresults(
        results = request.json['results'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/mlserver/trainingresults/<int:id>', methods = ['DELETE'])
def delete_trainingresults(id):
    entity = trainingresults.Trainingresults.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 200
