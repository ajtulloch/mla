from app import app
from app.queue import queue
import threading

threading.Thread(target=queue.start_training_queue).start()

app.run(debug = True)
