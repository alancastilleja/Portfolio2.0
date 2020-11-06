from flask import Flask
app = Flask(__name__)

from website.core.views import core
from website.error_handler.handler import error_handler

app.register_blueprint(core)
app.register_blueprint(error_handler)
