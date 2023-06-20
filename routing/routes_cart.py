from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from flask_cors import CORS, cross_origin
from subsidiary_functions import *
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from log_config import logging
from items import items, metodos
import time
import os

cart_pages = Blueprint('cart', __name__,
                        template_folder='Templates', static_folder='static', url_prefix = "/")

@cart_pages.route("/cart", methods = ["POST"])
def cart_post():
    return redirect("/") if request.form['submit'] == 'b' else post_with_searchbar()

@cart_pages.route("/cart")
def cart():

    if current_user.is_anonymous:
        return render_template("cart.html", items = items)
    loggedinuser = current_user.username
    return render_template("cart.html", loggedinuser=loggedinuser, is_admin = current_user.is_admin, items = items)