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


def on_report(ch, method, properties, body):
    # Writes the recieved response to the DB
    log.info("Recieved report: %s", body)
    request = ml_pb2.TrainingReport()
    request.ParseFromString(body)

    log.info("Parsed report to request: %s", request)
    entity = TrainingResults.TrainingResults(jsonString=request.jsonString)
    db.session.add(entity)
    db.session.commit()

    log.info("Saved entity to db: %s", entity)


def send_batch_training_request(request):
    log.info("Sending batch request: %s", request)
    channel.basic_publish(
        exchange='',
        routing_key=app.config['TRAINING_QUEUE'],
        body=request.SerializeToString())
    log.info("Sent batch request: %s", request)
    return True


def start_training_queue():
    log.info("Starting report queue")
    channel.basic_consume(on_report, queue=app.config['REPORT_QUEUE'], no_ack=True)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()
    log.info("Finishing report queue")
