import argh
import gen.protobufs.ml_pb2 as ml_pb2
import logging
import pika
import worker

log = logging.getLogger(__name__)


def on_batch_training_task(channel, report_queue):
    def runner(ch, method, properties, body):
        try:
            log.info("Recieved message")
            request = ml_pb2.BatchTrainRequest()
            request.ParseFromString(body)
            log.info("Running training from message")
            report = worker.batch_train(request)
            log.info("Sending report: %s on queue %s", report, report_queue)
            channel.basic_publish(
                exchange='',
                routing_key=report_queue,
                body=report.SerializeToString())
            log.info("Published report: %s", report)
        except:
            log.exception("Exception running training request")
    return runner


def main(rabbit_mq, training_queue, report_queue):
    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_mq))
    channel = connection.channel()
    channel.queue_declare(queue=training_queue)
    channel.queue_declare(queue=report_queue)
    channel.basic_consume(
        on_batch_training_task(channel, report_queue),
        queue=training_queue,
        no_ack=True)
    try:
        channel.start_consuming()
    finally:
        channel.stop_consuming()
    connection.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    argh.dispatch_command(main)
