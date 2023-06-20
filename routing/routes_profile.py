from subsidiary_functions import *
from flask_login import login_required, current_user
from items import items, metodos
import time

profile_pages = Blueprint('profile', __name__,
                        template_folder='Templates', static_folder='static', url_prefix = "/")

@profile_pages.route("/profile", methods = ["POST"])
@login_required
def profile_post():

    return post_with_searchbar()

@profile_pages.route("/profile")
@login_required
def profile():

    loggedinuser = current_user.username
    profilecreated1 = current_user.datetime
    profilecreated = profilecreated1.strftime("%Y %m %d")
    return render_template("profile.html", loggedinuser=loggedinuser, profilecreated = profilecreated, is_admin = current_user.is_admin, items = items)