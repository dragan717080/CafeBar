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
        su1 = request.form['username']
        sp1 = request.form['password']
        check_login = User.query.filter_by(username=su1).first()

        if check_login is None and current_user.is_anonymous:
            return redirect('/')

        passwords_match = check_login.password == sp1
        if check_login:
            if not passwords_match:
                new_blogs = []
                for i in range(min(3, len(Blog.query.all()))):
                    new_blogs.append(Blog.query.all()[i])

                return render_template('index.html', new_blogs=new_blogs, items=items)
            else:
                login_user(check_login)
                session['username'] = current_user.username
                new_blogs = []
                for blog in Blog.query.all()[:3]:
                    new_blogs.append([blog.title.capitalize(), blog.content.capitalize(), blog.author])

                return render_template('index.html', loggedinuser=current_user.username, new_blogs=new_blogs, is_admin=current_user.is_admin, items=items)

        return redirect('/')
    else:
        # posting via searchbar
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
    item1 = item_data['title']
    item2 = id
    item3 = item_data['pricing']
    item4 = item_data['imagesource']

    template_args = {
        'items': items,
        'item1': item1,
        'item2': item2,
        'item3': item3,
        'item4': item4
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
