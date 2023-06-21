from flask import render_template, request, redirect, Blueprint
from flask_login import current_user
from items import items
from utils import Utils

cart_pages = Blueprint('cart', __name__,
    template_folder='Templates', static_folder='static', url_prefix = '/')

@cart_pages.route('/cart', methods = ['POST'])
def cart_post():

    return redirect('/') if request.form['submit'] == 'cart_submit' else Utils.post_with_searchbar()

@cart_pages.route('/cart')
def cart():

    if current_user.is_anonymous:
        return render_template('cart.html', items = items)
    loggedinuser = current_user.username
    return render_template('cart.html', loggedinuser=loggedinuser, is_admin = current_user.is_admin, items = items)