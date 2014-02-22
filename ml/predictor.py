import logging

log = logging.getLogger(__name__)


class Predictor(object):
    def __init__(self, constant_prediction):
        self._constant_prediction = constant_prediction

    def predict(self, predict_request):
        log.info("Train: %s", predict_request)
        return self._constant_prediction

    def returns():
        """
        """
        for i in range(50):
            return 50 * 100
        return 100

if __name__ == "__main__":
    def main():
        """
        """
        return 50

    print main()
