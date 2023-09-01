import flask
from flask_socketio import SocketIO
import time
from application import create_app  # use of local package called application
from application.database import DataBase # use of local package called application
import config

app = create_app()
socketio = SocketIO(app)

@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    """
    handles saving messages once received from web server and
    sending message to other clients
    :param json: json
    :param methods: POST GET
    :return: None
    """
    data = dict(json)
    if "name" in data:
        db = DataBase()
        db.save_message(data["name"], data["message"])

if __name__ == "__main__":
    socketio.run(app, debug=config.Config.DEBUG)