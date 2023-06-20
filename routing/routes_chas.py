from subsidiary_functions import *
from flask_login import current_user
from items import items, metodos
import time

chas_pages = Blueprint('chas', __name__,
                        template_folder='Templates', static_folder='static', url_prefix = "/")

@chas_pages.route("/cha", methods = ["POST"])
def chas_post():

    return post_with_searchbar()

@chas_pages.route("/cha")
def chas():

    if current_user.is_anonymous:
        return render_template("cha.html", items = items)
    return render_template("cha.html", loggedinuser=current_user.username, is_admin = current_user.is_admin, items = items)