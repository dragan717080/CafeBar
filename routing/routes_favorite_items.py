from subsidiary_functions import *
from flask_login import current_user
from items import items, metodos
import time

favorite_items_pages = Blueprint('favorites', __name__,
                        template_folder='Templates', static_folder='static', url_prefix = "/")

@favorite_items_pages.route("/fav", methods = ["POST"])
def favorite_items_post():

        return post_with_searchbar()

@favorite_items_pages.route("/fav")

def favorite_items():
    if current_user.is_anonymous:
        return render_template("fav.html", items = items)
    loggedinuser = current_user.username
    return render_template("fav.html", loggedinuser=current_user.username, is_admin = current_user.is_admin, items = items)