from app import app
from app.queue import queue
import threading
import logging

logging.basicConfig(level=logging.INFO)

threading.Thread(target=queue.start_training_report_queue).start()

app.run(debug = True)
