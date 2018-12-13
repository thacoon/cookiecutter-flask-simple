import os

from flask import Flask

from config import config


CONFIG = os.getenv('CONFIG') or 'default'


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    from .core import core as core_blueprint
    app.register_blueprint(core_blueprint)

    return app
