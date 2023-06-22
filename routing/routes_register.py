from flask import request, redirect, render_template, Blueprint, session
from flask_login import login_user, current_user
from items import items, admins
from db_models import User

register_pages = Blueprint('register', __name__,
    template_folder='Templates', static_folder='static', url_prefix = '/')

@register_pages.route('/register', methods = ['POST'])
def register_post():

    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    user_data = {
        'email': email,
        'username': username,
        'password': password
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

    return render_template('register.html', items=items)