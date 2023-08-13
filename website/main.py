import flask
from flask_socketio import SocketIO
import time
from application import create_app  # use of local package called application
from application.database import DataBase # use of local package called application
import config

app = create_app()
socketio = SocketIO(app)
