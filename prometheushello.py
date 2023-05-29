from flask import Flask
import time
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

app = Flask(__name__)

@app.route('/hello1')
def index():
    time.sleep(1)
    return 'Web App with Python Flask hello1!'

@app.route('/hello2')
def hello2():
    time.sleep(5)
    return 'Web App with Python Flask! hello2'

app.run(host='0.0.0.0', port=8888)