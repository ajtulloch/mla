import ml
import json
import logging

import gen.protobufs.ml_pb2 as ml_pb2

log = logging.getLogger(__name__)


def batch_train(request):
    log.debug("Creating report for request: %s", request)
    assert request.trainingData.source == ml_pb2.INLINE
    report = ml_pb2.TrainingReport(
        jsonResult=json.dumps(
            ml.Reporter.report(request.trainingData.inlineData)))
    log.debug("Report constructed: %s", report)
    return report
