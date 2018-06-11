from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_first_blue


def create_app():
    app = Flask(__name__)

    app.config.from_object(envs.get("develop"))

    init_first_blue(app)

    init_ext(app)

    return app