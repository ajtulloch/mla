import requests
import util.protobuf_json as protobuf_json
import util.random_data as random_data
import logging
import json

log = logging.getLogger(__name__)


def send_batch_request(url, num_features=3, num_examples=10):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    request = \
        random_data.random_batch_training_request(num_features, num_examples)
    data = protobuf_json.pb2json(request)
    log.info("Sending request JSON: %s", data)

    return requests.post(url, data=json.dumps(data), headers=headers)
