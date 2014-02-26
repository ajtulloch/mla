import util.random_data as random_data
import client.py.client as client
import logging

log = logging.getLogger(__name__)


def send_batch_request(
        url,
        mnist=False,
        target=5,
        num_features=100,
        num_examples=1000):
    c = client.MLApplianceClient(url)
    if mnist:
        log.info("Generating MNIST data")
        dataset = random_data.mnist_label_feature_pairs(target=target)
    else:
        log.info("Generating random data")
        dataset = (random_data.label_feature_pair(num_features=100)
                   for _ in range(num_examples))
    return c.batch_train(list(dataset)[:num_examples])
