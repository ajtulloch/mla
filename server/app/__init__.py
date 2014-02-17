import dataset

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from ml import Trainer, Predictor, Storage


app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)

storage = Storage(db=dataset.connect(app.config['ML_STORAGE_DB']))
trainer = Trainer()
predictor = Predictor(constant_prediction=0.05)

from app.routes import index
from app.routes import mlmodels
from app.routes import labeledpoints
from app.routes import train
from app.routes import predict
from app.routes import datasets
from app.routes import trainingresults
