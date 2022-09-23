from flask import Flask, render_template, url_for, redirect, session
import os
from datetime import timedelta



app = Flask(__name__)

app.config.from_object("config")

from app.homepage.index import index_module

app.register_blueprint(index_module)

from app.user_controller.user_controller import user_module

app.register_blueprint(user_module)

from app.shopping.cart import cart_module

app.register_blueprint(cart_module)

# @app.errorhandler(404)
# def not_found(error):
#     return render_template("404.html")



@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=3000)


@app.before_first_request
def make_session():
    session['cart_list'] = []