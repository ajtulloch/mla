from app import app, trainer
from flask import request, jsonify
import gen.protobufs.ml_pb2 as pb
from protobuf_to_dict import protobuf_to_dict


@app.route('/train', methods=['POST'])
def train():
    req = pb.TrainRequest(
        features=request.json['features'],
        label=request.json['label']
    )
    trainer.train(req)
    resp = pb.TrainResponse()
    return jsonify(protobuf_to_dict(resp)), 200


@app.route('/predict', methods=['GET'])
def predict():
    print "Predict"
    req = pb.PredictRequest(
        features=request.json['features'],
    )
    prediction = trainer.predict(req)

    resp = pb.PredictResponse(prediction=prediction)
    return jsonify(protobuf_to_dict(resp)), 200

