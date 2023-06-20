from subsidiary_functions import *
from flask_login import login_user, current_user
from items import items, admins

register_pages = Blueprint('register', __name__,
                        template_folder='Templates', static_folder='static', url_prefix = '/')

@register_pages.route('/register', methods = ['POST'])
def register_post():

    email = request.form['email']
    username = request.form['username_11']
    password = request.form['password_11']
    user_data = {
        'email': email,
        'username': username,
        'password': password
    }
    nu = User(**user_data)
    if nu.username in admins:
        nu.is_admin = True
    db.session.add(nu)
    db.session.commit()
    login_user(nu)
    session['username'] = current_user.username
    return redirect('/')

@register_pages.route('/register')
def register():

    return render_template('register.html', items=items)