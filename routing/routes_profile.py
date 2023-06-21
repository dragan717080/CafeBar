from flask import render_template, Blueprint
from flask_login import login_required, current_user
from utils import Utils
from items import items

profile_pages = Blueprint('profile', __name__,
    template_folder='Templates', static_folder='static', url_prefix = '/')

@profile_pages.route('/profile', methods = ['POST'])
@login_required
def profile_post():

    return Utils.post_with_searchbar()

@profile_pages.route('/profile')
@login_required
def profile():

    user_data = {
        'loggedinuser': current_user.username,
        'profilecreated': current_user.created_at.strftime('%Y %m %d'),
        'is_admin' : current_user.is_admin,
        'items': items
    }

    return render_template('profile.html', **user_data)
