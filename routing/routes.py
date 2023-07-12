from flask import request, redirect, render_template, Blueprint, session
from db_models import User, Blog
from utils import Utils
from flask_login import login_user, current_user
from items import items

index_pages = Blueprint('index', __name__,
    template_folder='Templates', static_folder='static', url_prefix = '/')

@index_pages.route('/', methods=['POST'])
def index_post():
    if request.form['submit'] == 'LOGIN':
        username = request.form['username']
        password = request.form['password']
        check_login = User.find(username=username)
        if check_login is None and current_user.is_anonymous:
            return redirect('/')

        passwords_match = check_login.password == password
        if check_login:
            new_blogs = Blog.query.limit(3).all()
            if not passwords_match:
                return render_template('index.html', new_blogs=new_blogs, items=items)
            else:
                login_user(check_login)
                session['username'] = current_user.username
                new_blogs = Blog.query.limit(3).all()
                new_blogs = [[blog.title.capitalize(), blog.content.capitalize(), blog.author] for blog in new_blogs]
                return render_template('index.html', loggedinuser=current_user.username, new_blogs=new_blogs, is_admin=current_user.is_admin, items=items)

        return redirect('/')
    else:
        return Utils.post_with_searchbar()

@index_pages.route('/')
def index():
    new_blogs = [[blog.title.capitalize(), blog.content.capitalize(), blog.author] for blog in
        Blog.query.all()[:3]]

    if current_user.is_anonymous:
        return render_template('index.html', new_blogs=new_blogs, items=items)

    return render_template('index.html', loggedinuser=current_user.username, is_admin=current_user.is_admin,
        new_blogs=new_blogs, items=items)

@index_pages.route('/<int:id>')
def get_item(id):
    item_data = items[id]
    title = item_data['title']
    pricing = item_data['pricing']
    imagesource = item_data['imagesource']

    template_args = {
        'items': items,
        'title': title,
        'pricing': pricing,
        'imagesource': imagesource
    }
    if current_user.is_anonymous:
        return render_template('item.html', **template_args)

    template_args.update({
        'loggedinuser': current_user.username,
        'is_admin': current_user.is_admin
    })
    return render_template('item.html', **template_args)


@index_pages.route('/<int:id>', methods=['POST'])
def post_item(id):
    
    return Utils.post_with_searchbar()
