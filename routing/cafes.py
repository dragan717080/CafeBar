from flask import render_template, Blueprint
from flask_login import current_user
from utils import *
from items import items

cafes_pages = Blueprint('cafes', __name__,
    template_folder='Templates', static_folder='static', url_prefix = "/")

@cafes_pages.route("/cafes", methods = ["POST"])
def cafes_post():
    return Utils.post_with_searchbar()

@cafes_pages.route("/cafes")
def cafes():
    if current_user.is_anonymous:
        return render_template("cafes.html", items = items)

    return render_template("cafes.html", loggedinuser=current_user.username, is_admin = current_user.is_admin, items = items)
