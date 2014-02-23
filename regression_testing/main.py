import argh
import generator
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    argh.dispatch_command(generator.send_batch_request)
