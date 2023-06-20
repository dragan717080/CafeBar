from subsidiary_functions import *
from flask_login import current_user
from items import items, metodos
import time

emporio_pages = Blueprint('emporio', __name__,
                        template_folder='Templates', static_folder='static', url_prefix = "/")

@emporio_pages.route("/emporio", methods = ["POST"])
def emporio_post():

    return post_with_searchbar()

@emporio_pages.route("/emporio")
def emporio():

    if current_user.is_anonymous:
        return render_template("emporio.html", items = items)
    return render_template("emporio.html", loggedinuser=current_user.username, is_admin=current_user.is_admin, items = items)