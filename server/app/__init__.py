from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from ml import Trainer

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)


from app.models import mlmodel
from app.models import labeledpoint
from app.routes import index

from app.routes import mlmodels
from app.routes import labeledpoints
