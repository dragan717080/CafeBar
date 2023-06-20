from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from flask_cors import CORS, cross_origin
from subsidiary_functions import *
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from log_config import logging
from items import items, metodos
import time
import os

all_users_pages = Blueprint('all_users', __name__,
                        template_folder='Templates', static_folder='static', url_prefix = "/")

@all_users_pages.route("/allusers")
@login_required
def allusers():
    users = User.query.all()
    u_list = []

    for user in users:
        u_list.append({
            "email": user.email,
            "username": user.username,
            "is_admin": user.is_admin
        })

    return jsonify({"All registered users": u_list})
