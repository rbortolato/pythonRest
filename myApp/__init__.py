from flask import Flask
from myApp.endpoint.premios import premiosEndpoint
from myApp.controller.readFile import read
from myApp.database import initialize

app = Flask('__name___')
app.register_blueprint(premiosEndpoint)

initialize()
read()