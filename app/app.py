import time

from app.infrastructure.views import blueprint
from flask import Flask

app = Flask(__name__)
app.register_blueprint(blueprint)
