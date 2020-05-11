from flask import Flasklu
from flask_bootstrap import Bootstrap


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .api import api as blueprint_api
    app.register_blueprint(blueprint=blueprint_api,
                           url_prefix = 'apiv1')


