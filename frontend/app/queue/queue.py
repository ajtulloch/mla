from app import db, app
from app.models import TrainingResults
import pika
import gen.protobufs.ml_pb2 as ml_pb2
import util.protobuf_json as protobuf_json
import logging
import json

log = logging.getLogger(__name__)

CONNECTION = None
CHANNEL = None

def on_report(ch, method, properties, body):
    # Writes the recieved response to the DB
    try:
        log.info("Recieved report")
        request = ml_pb2.TrainingReport()
        request.ParseFromString(body)

        log.info("Parsed report to request: %s", request)
        entity = TrainingResults.TrainingResults(
            jsonReport=json.dumps(protobuf_json.pb2json(request)))
        db.session.add(entity)
        db.session.commit()
        log.info("Saved entity to db: %s", entity)
    except:
        log.exception("Exception in reporting")


def send_batch_training_request(request):
    log.info("Sending batch request to queue")
    log.debug("Sending batch request: %s", request)
    CHANNEL.basic_publish(
        exchange='',
        routing_key=app.config['TRAINING_QUEUE'],
        body=request.SerializeToString())
    log.debug("Sent batch request: %s", request)
    log.info("Sent batch request")


def start_training_report_queue():
    global CONNECTION
    CONNECTION = pika.BlockingConnection(pika.ConnectionParameters(app.config['RABBITMQ']))
    CHANNEL = CONNECTION.channel()
    CHANNEL.queue_declare(queue=app.config['TRAINING_QUEUE'])
    CHANNEL.queue_declare(queue=app.config['REPORT_QUEUE'])

    log.info("Starting report queue")
    CHANNEL.basic_consume(on_report, queue=app.config['REPORT_QUEUE'], no_ack=True)
    try:
        CHANNEL.start_consuming()
    except Exception:
        log.exception("Got exception consuming on the training report queue")
    finally:
        CHANNEL.stop_consuming()
    CONNECTION.close()
    log.info("Finishing report queue")
