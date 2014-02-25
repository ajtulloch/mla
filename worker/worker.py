from ml.report import ProtobufReporter
import logging
import gen.protobufs.ml_pb2 as ml_pb2

log = logging.getLogger(__name__)


def get_training_data(request):
    if request.trainingData.source != ml_pb2.INLINE:
        raise NotImplemented
    return request.trainingData.inlineData


def batch_train(request):
    log.debug("Creating report for request: %s", request)
    training_data = get_training_data(request)
    report = ProtobufReporter().build(training_data)
    log.debug("Report constructed: %s", report)
    return report
