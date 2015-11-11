from bottle import Bottle, run
from bottle.ext.mongo import MongoPlugin
from bson.json_util import dumps
from config.routes import *

import click
import os

app = Bottle()
plugin = MongoPlugin(uri="mongodb://127.0.0.1", db="mentorfy", json_mongo=True)
app.install(plugin)

setup_routes(app)

@click.group()
def cmds():
    pass


@cmds.command()
@click.option('--port', default=os.environ.get('PORT', 8080), type=int,
              help=u'Set application server port!')
@click.option('--ip', default='0.0.0.0', type=str,
              help=u'Set application server ip!')
@click.option('--debug', default=False,
              help=u'Set application server debug!')
def runserver(port, ip, debug):
    click.echo('Start server at: {}:{}'.format(ip, port))
    run(app=app, host=ip, port=port, debug=debug, reloader=debug)


@cmds.command()
def test():
    import pytest
    pytest.main(['-x', 'tests'])


if __name__ == "__main__":
    cmds()
