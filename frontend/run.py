from app import app
from app.queue import queue
import threading
import logging

logging.basicConfig(level=logging.INFO)

# Fire up queue thread
queue_thread = threading.Thread(target=queue.start_training_report_queue)
queue_thread.daemon = True
queue_thread.start()

app.run(debug = True)
