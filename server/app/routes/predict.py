from app import app, predictor
from flask import request, jsonify
import gen.protobufs.ml_pb2 as pb
from protobuf_to_dict import protobuf_to_dict


@app.route('/predict', methods=['POST'])
def predict():
    print "Predict"
    req = pb.PredictRequest(
        features=request.json['features'],
    )
    prediction = predictor.predict(req)
    resp = pb.PredictResponse(prediction=prediction)
    return jsonify(protobuf_to_dict(resp)), 200
