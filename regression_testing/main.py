import argh
import generator
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    argh.dispatch_command(generator.send_batch_request)
