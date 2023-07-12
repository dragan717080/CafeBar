from flask import render_template, request, redirect, Blueprint
from flask_login import login_user, current_user
from config.log_config import logging
from db_models import User

login_pages = Blueprint('login', __name__)
all_users = User.find_all()

@login_pages.route('/login', methods = ['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    existing_user = User.find(username=username)
    if existing_user == None and current_user.is_anonymous:
        return render_template('login.html')
    passwords_match = existing_user.password == password
    if existing_user:
        if not passwords_match:
            user = User.find(username=username)
            user.password='asdasdasd'
            user.save()
            return render_template('login.html', all_users=all_users, passwords_not_matching=1)
        else:
            login_user(existing_user)
            return redirect('/')
    return redirect('/')

@login_pages.route('/login')
def login():
    return render_template('login.html', all_users=all_users)
