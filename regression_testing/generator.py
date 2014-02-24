import util.random_data as random_data
import client.py.client as client
import logging

log = logging.getLogger(__name__)


def send_batch_request(url, num_features=3, num_examples=10):
    c = client.MLApplianceClient(url)
    return c.batch_train(random_data.label_feature_pair(num_features)
                         for _ in range(num_examples))
