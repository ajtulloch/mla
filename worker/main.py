import argh
import gen.protobufs.ml_pb2 as ml_pb2
import logging
import pika
import worker

log = logging.getLogger(__name__)


def on_batch_training_task(channel, report_queue):
    def runner(ch, method, properties, body):
        request = ml_pb2.BatchTrainRequest()
        request.ParseFromString(body)
        report = worker.batch_train(request)
        channel.basic_publish(
            exchange='',
            routing_key='hello',
            body=report.SerializeToString())
    return runner


def main(rabbit_mq, training_queue, report_queue):
    connection = pika.BlockingConnection(pika.ConnectionParameters(rabbit_mq))
    channel = connection.channel()
    channel.queue_declare(queue=training_queue)
    channel.queue_declare(queue=report_queue)
    channel.basic_consume(
        worker.on_batch_training_task(channel, report_queue),
        queue=training_queue,
        no_ack=True)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()

if __name__ == "__main__":
    argh.dispatch_command(main)
