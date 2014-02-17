import logging

log = logging.getLogger(__name__)


class Predictor(object):
    def __init__(self, constant_prediction):
        self._constant_prediction = constant_prediction

    def predict(self, predict_request):
        log.info("Train: %s", predict_request)
        return self._constant_prediction
