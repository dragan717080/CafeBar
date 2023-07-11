from flask import request, redirect, render_template, Blueprint, session
from flask_login import login_user, current_user
from items import admins
from db_models import User
from utils import Utils

register_pages = Blueprint('register', __name__)

@register_pages.route('/register', methods = ['POST'])
def register_post():
    if not 'email' in request.form: return Utils.post_with_searchbar()
    user_data = {
        'email': request.form['email'],
        'username': request.form['username'],
        'password': request.form['password']
    }
    new_user = User(**user_data)
    if new_user.username in admins:
        new_user.is_admin = True
    User.save(new_user)
    login_user(new_user)
    session['username'] = current_user.username
    return redirect('/')

@register_pages.route('/register')
def register():
    return render_template('register.html', all_users = User.find_all())
