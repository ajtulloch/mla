import util.random_data as random_data
import client.py.client as client
import logging

log = logging.getLogger(__name__)


def send_batch_request(url, target=5, num_examples=1000):
    c = client.MLApplianceClient(url)
    dataset = list(random_data.mnist_label_feature_pairs(target=target))
    return c.batch_train(dataset[:num_examples])
