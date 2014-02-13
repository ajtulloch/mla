from app import app, db
from app.models import labeledpoint
from flask import abort, jsonify, request
import datetime
import json

@app.route('/mlserver/labeledpoints', methods = ['GET'])
def get_all_labeledpoints():
    entities = labeledpoint.Labeledpoint.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/mlserver/labeledpoints/<int:id>', methods = ['GET'])
def get_labeledpoint(id):
    entity = labeledpoint.Labeledpoint.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/mlserver/labeledpoints', methods = ['POST'])
def create_labeledpoint():
    entity = labeledpoint.Labeledpoint(
        label = request.json['label']
        , features = request.json['features']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/mlserver/labeledpoints/<int:id>', methods = ['PUT'])
def update_labeledpoint(id):
    entity = labeledpoint.Labeledpoint.query.get(id)
    if not entity:
        abort(404)
    entity = labeledpoint.Labeledpoint(
        label = request.json['label'],
        features = request.json['features'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/mlserver/labeledpoints/<int:id>', methods = ['DELETE'])
def delete_labeledpoint(id):
    entity = labeledpoint.Labeledpoint.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 200
