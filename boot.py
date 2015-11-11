from bottle import Bottle, run
# from app.controllers import *
# from app.models import *
from config.routes import *

app = Bottle()

setup_routes(app)
run(app, host='localhost', port=8080)
