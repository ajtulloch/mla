from app import app, db
from app.models import dataset
from flask import abort, jsonify, request
import datetime
import json

@app.route('/mlserver/datasets', methods = ['GET'])
def get_all_datasets():
    entities = dataset.Dataset.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/mlserver/datasets/<int:id>', methods = ['GET'])
def get_dataset(id):
    entity = dataset.Dataset.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/mlserver/datasets', methods = ['POST'])
def create_dataset():
    entity = dataset.Dataset(
        name = request.json['name']
        , examples = request.json['examples']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/mlserver/datasets/<int:id>', methods = ['PUT'])
def update_dataset(id):
    entity = dataset.Dataset.query.get(id)
    if not entity:
        abort(404)
    entity = dataset.Dataset(
        name = request.json['name'],
        examples = request.json['examples'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/mlserver/datasets/<int:id>', methods = ['DELETE'])
def delete_dataset(id):
    entity = dataset.Dataset.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 200
