from bottle import route
from app.controllers import application_controller 

def setup_routes(app):
    app.route('/', 'GET', application_controller.index)
    app.route('/images/<filename:re:.*\.jpg>', 'GET', application_controller.images)
