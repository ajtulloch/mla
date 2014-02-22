from app import db, app
from app.models import TrainingResults
import pika
import gen.protobufs.ml_pb2 as ml_pb2

import logging

log = logging.getLogger(__name__)

connection = pika.BlockingConnection(pika.ConnectionParameters(app.config['RABBITMQ']))
channel = connection.channel()
channel.queue_declare(queue=app.config['TRAINING_QUEUE'])
channel.queue_declare(queue=app.config['REPORT_QUEUE'])


def on_report():
    def runner(ch, method, properties, body):
        # Writes the recieved response to the DB
        request = ml_pb2.TrainingReport()
        request.ParseFromString(body)
        entity = TrainingResults.TrainingResults(
            jsonString=request.jsonString
        )
        db.session.add(entity)
        db.session.commit()
    return runner


def send_batch_training_request(request):
    channel.basic_publish(
        exchange='',
        routing_key=app.config['REPORT_QUEUE'],
        body=request.SerializeToString())
    return True


def start_training_queue():
    channel.basic_consume(on_report(), queue=app.config['TRAINING_QUEUE'], no_ack=True)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()
