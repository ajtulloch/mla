import logging

log = logging.getLogger(__name__)


class Trainer(object):
    def __init__(self):
        self._models = []

    def train(self, train_request):
        log.info("Train: %s", train_request)
        pass
