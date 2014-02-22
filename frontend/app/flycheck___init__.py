from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)


from app.models import TrainingResults
from app.models import BatchTrainingRequest
from app.routes import index

from app.routes import Trainingresults
from app.routes import Batchtrainingrequests
