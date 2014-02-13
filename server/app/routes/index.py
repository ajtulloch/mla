from app import app
from ml import Trainer

@app.route('/')
def root():
    return app.send_static_file('index.html')


