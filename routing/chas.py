from flask import render_template, Blueprint
from flask_login import current_user
from utils import Utils
from items import items

chas_pages = Blueprint('chas', __name__)

@chas_pages.route("/cha", methods = ["POST"])
def chas_post():
    return Utils.post_with_searchbar()

@chas_pages.route("/cha")
def chas():
    if current_user.is_anonymous:
        return render_template("cha.html", items = items)

    return render_template("cha.html", loggedinuser=current_user.username, is_admin = current_user.is_admin, items = items)
