from subsidiary_functions import *
from flask_login import current_user
from items import items, metodos
import time

cafes_pages = Blueprint('cafes', __name__,
                        template_folder='Templates', static_folder='static', url_prefix = "/")

@cafes_pages.route("/cafes", methods = ["POST"])
def cafes_post():
    return post_with_searchbar()

@cafes_pages.route("/cafes")
def cafes():

    if current_user.is_anonymous:
        return render_template("cafes.html", items = items)
    return render_template("cafes.html", loggedinuser=current_user.username, is_admin = current_user.is_admin, items = items)
