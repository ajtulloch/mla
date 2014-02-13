import logging

log = logging.getLogger(__name__)



class Trainer(object):
    """
    """
    
    def __init__(self):
        pass

    def train(self, train_request):
        """
        
        Arguments:
        - `train_request`:
        """
        log.info("Train: %s", train_request)
        pass


class Predictor(object):
    """
    """
    
    def __init__(self, constant_prediction):
        """
        
        Arguments:
        - `constant_prediction`:
        """
        self._constant_prediction = constant_prediction
        return

    def predict(self, predict_request):
        """
        
        Arguments:
        - `predict_request`:
        """
        log.info("Train: %s", predict_request)
        return self._constant_prediction
