import pika
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


def persist(channel, report):
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=report.SerializeToString())

def on_batch_training_task(channel):
    def runner(ch, method, properties, body):
        request = ml_pb2.BatchTrainRequest()
        request.ParseFromString(body)
        report = batch_train(request)
        persist(channel, request, report)
    return runner


def random_data():
    return ml_pb2.OnlineTrainRequest(
        features=[random.random() for _ in range(100)],
        label=random.choice([True, False]))


def test():
    req = ml_pb2.BatchTrainRequest(
        trainingData=ml_pb2.TrainingData(
            source=ml_pb2.INLINE,
            inlineData=[random_data() for _ in range(100)]))
    return batch_train(req)


def main(db_connection, rabbit_mq, training_queue, results):
    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_mq))
    channel = connection.channel()
    channel.queue_declare(queue=training_queue)
    channel.basic_consume(
        on_batch_training_task,
        queue=training_queue,
        no_ack=True)

# if __name__ == "__main__":
#     # poll work queue for jobs
#     # run job.
#     # argh.dispatch_command(main)          
#     sys.exit(0)
