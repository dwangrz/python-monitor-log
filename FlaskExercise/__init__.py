import logging
from flask import Flask

app = Flask(__name__)
wsgi_app = app.wsgi_app
logger = logging.getLogger(__name__)
#   Set the app's logger level to "warning"
#   and any other necessary changes
logger.setLevel(logging.WARNING)
steamHandler = logging.StreamHandler()
steamHandler.setLevel(logging.WARNING)
logger.addHandler(steamHandler)


import FlaskExercise.views