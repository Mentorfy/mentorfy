from bottle import Bottle, run
from app.controllers import *
from app.models import *

app = Bottle()
run(app, host='localhost', port=8080)
