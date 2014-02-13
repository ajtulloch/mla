import logging

log = logging.getLogger(__name__)


class Trainer(object):
    """
    """
    
    def __init__(self, prediction):
        """
        
        Arguments:
        - `prediction`:
        """
        self._prediction = prediction

    def predict(self, predict_request):
        log.info("Prediction: %s", predict_request)
        return self.prediction

    def train(self, train_request):
        """
        
        Arguments:
        - `train_request`:
        """
        log.info("Train: %s", train_request)
        pass
