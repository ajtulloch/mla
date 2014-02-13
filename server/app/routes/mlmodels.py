from app import app, db
from app.models import mlmodel
from flask import abort, jsonify, request
import datetime
import json

@app.route('/mlserver/mlmodels', methods = ['GET'])
def get_all_mlmodels():
    entities = mlmodel.Mlmodel.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/mlserver/mlmodels/<int:id>', methods = ['GET'])
def get_mlmodel(id):
    entity = mlmodel.Mlmodel.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/mlserver/mlmodels', methods = ['POST'])
def create_mlmodel():
    entity = mlmodel.Mlmodel(
        name = request.json['name']
        , serialized = request.json['serialized']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/mlserver/mlmodels/<int:id>', methods = ['PUT'])
def update_mlmodel(id):
    entity = mlmodel.Mlmodel.query.get(id)
    if not entity:
        abort(404)
    entity = mlmodel.Mlmodel(
        name = request.json['name'],
        serialized = request.json['serialized'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/mlserver/mlmodels/<int:id>', methods = ['DELETE'])
def delete_mlmodel(id):
    entity = mlmodel.Mlmodel.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 200
