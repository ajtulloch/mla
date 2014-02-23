from app import app, db
from app.models import BatchTrainingRequest
from flask import abort, jsonify, request
import datetime
import json
import logging

import util.protobuf_json as protobuf_json
import gen.protobufs.ml_pb2 as ml_pb2
from app.queue import queue

log = logging.getLogger(__name__)

@app.route('/app/Batchtrainingrequests', methods = ['GET'])
def get_all_Batchtrainingrequests():
    entities = BatchTrainingRequest.BatchTrainingRequest.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/app/Batchtrainingrequests/<int:id>', methods = ['GET'])
def get_BatchTrainingRequest(id):
    entity = BatchTrainingRequest.BatchTrainingRequest.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/app/Batchtrainingrequests', methods = ['POST'])
def create_BatchTrainingRequest():
    log.info("Request: %s", request)
    log.info("Request data: %s", request.data)
    log.info("Request JSON: %s", request.json)
    entity = BatchTrainingRequest.BatchTrainingRequest(
        trainingData = json.dumps(request.json['trainingData'])
    )
    db.session.add(entity)
    db.session.commit()

    log.info("Batch training entity committed")
    log.debug("Batch training entity committed: %s ", entity)

    # fire off the batch training request to the worker queue
    req = ml_pb2.BatchTrainRequest()
    req = protobuf_json.json2pb(req, request.json)
    queue.send_batch_training_request(req)

    log.info("Batch training req sent to queue")
    log.debug("Batch training req sent to queue: %s", req)
    return jsonify(entity.to_dict()), 201

@app.route('/app/Batchtrainingrequests/<int:id>', methods = ['PUT'])
def update_BatchTrainingRequest(id):
    entity = BatchTrainingRequest.BatchTrainingRequest.query.get(id)
    if not entity:
        abort(404)
    entity = BatchTrainingRequest.BatchTrainingRequest(
        trainingData = request.json['trainingData'],
        id = id
    )

    db.session.merge(entity)
    db.session.commit()

    # fire off the batch training request to the worker queue
    req = ml_pb2.BatchTrainRequest()
    req = protobuf_json(req, request.json)
    queue.send_batch_training_request(req)
    return jsonify(entity.to_dict()), 201

@app.route('/app/Batchtrainingrequests/<int:id>', methods = ['DELETE'])
def delete_BatchTrainingRequest(id):
    entity = BatchTrainingRequest.BatchTrainingRequest.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 200
