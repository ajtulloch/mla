from app import app, trainer, storage
from flask import request, jsonify
import gen.protobufs.ml_pb2 as pb
from protobuf_to_dict import protobuf_to_dict


@app.route('/datasetimport', methods=['POST'])
def train():
    req = pb.DataSetImportRequest(
        examples=request.json['examples']
        datasetName=request.json['datasetName']
    )
    storage.add(req)
    trainer.train(req)
    resp = pb.TrainResponse()
    return jsonify(protobuf_to_dict(resp)), 200
