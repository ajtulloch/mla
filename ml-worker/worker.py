
import ml
import random
import json
import logging

import gen.protobufs.ml_pb2 as ml_pb2

log = logging.getLogger(__name__)


def batch_train(request):
    assert request.trainingData.source == ml_pb2.INLINE
    return ml_pb2.TrainingReport(
        jsonResult=json.dumps(
            ml.Reporter.report(request.trainingData.inlineData)))


def persist(channel, report_queue, report):
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=report.SerializeToString())
    return True


def on_batch_training_task(channel, report_queue):
    def runner(ch, method, properties, body):
        request = ml_pb2.BatchTrainRequest()
        request.ParseFromString(body)
        report = batch_train(request)
        persist(channel, report_queue, report)
    return runner
