# this file was created to indicate that the parent directory (application) is a python package
from flask import Flask

def create_app():
    pass
    '''Construct the core application'''
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Imports
