from app import app
from app.queue import queue
import threading
import logging
from flask_appconfig.heroku import from_heroku_envvars

logging.basicConfig(level=logging.INFO)

from_heroku_envvars(app.config)

if app.config['ENABLE_QUEUE']:
# Fire up queue thread
    queue_thread = threading.Thread(target=queue.start_training_report_queue)
    queue_thread.daemon = True
    queue_thread.start()

app.run(debug=True)
