import requests
import logging
import gen.protobufs.ml_pb2 as ml_pb2
import util.protobuf_json as protobuf_json
import json
import urlparse

log = logging.getLogger(__name__)


class MLApplianceClient(object):
    BATCH_TRAIN_PATH = "/app/Batchtrainingrequests"

    def __init__(self, host):
        self._host = host

    def _post(self, path, request_protobuf):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = protobuf_json.pb2json(request_protobuf)
        log.debug("Sending request JSON: %s", data)
        return requests.post(
            urlparse.urljoin(self._host, path),
            data=json.dumps(data),
            headers=headers)

    def batch_train(self, label_feature_pairs):
        online_train_requests = [ml_pb2.OnlineTrainRequest(
            features=features,
            label=label) for (label, features) in label_feature_pairs]

        batch_train_request = ml_pb2.BatchTrainRequest(
            trainingData=ml_pb2.TrainingData(
                source=ml_pb2.INLINE,
                inlineData=online_train_requests))
        return self._post(self.BATCH_TRAIN_PATH, batch_train_request)
