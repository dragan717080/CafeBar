from flask import render_template, Blueprint
from flask_login import login_required, logout_user, current_user
from items import items

logout_pages = Blueprint('logout', __name__,
    template_folder='Templates', static_folder='static', url_prefix = '/')

@logout_pages.route('/logout')
@login_required
def logout():

    user = current_user.username
    logout_user()
    return render_template('logout.html', currentuser=user, items=items)
