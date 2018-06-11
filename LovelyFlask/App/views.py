from flask import Blueprint, request, render_template

blue = Blueprint("first_blue", __name__, url_prefix="/api/")

def init_first_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route("/home/")
def home():

   return 'Hello Moto'




