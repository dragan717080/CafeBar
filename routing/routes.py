from subsidiary_functions import *
from flask_login import login_user, current_user
from log_config import logging
from items import items, metodos
import time

index_pages = Blueprint('index', __name__,
                        template_folder='Templates', static_folder='static', url_prefix = "/")

@index_pages.route("/", methods=["POST"])
def index_post():
    if request.form['submit'] == "LOGIN":
        su1 = request.form['username_1']
        sp1 = request.form['password_1']
        check_login = User.query.filter_by(username=su1).first()

        if check_login is None and current_user.is_anonymous:
            return redirect('/')

        passwords_match = check_login.password == sp1
        if check_login:
            if not passwords_match:
                listofnewblogs = []
                for i in range(min(3, len(Blog.query.all()))):
                    listofnewblogs.append(Blog.query.all()[i])

                return render_template("index.html", listofnewblogs=listofnewblogs, items=items)
            else:
                login_user(check_login)
                session['username'] = current_user.username
                listofnewblogs = []
                for blog in Blog.query.all()[:3]:
                    listofnewblogs.append([blog.title.capitalize(), blog.content.capitalize(), blog.author])

                return render_template("index.html", loggedinuser=current_user.username, listofnewblogs=listofnewblogs, is_admin=current_user.is_admin, items=items)

        return redirect("/")
    else:
        # posting via searchbar
        return post_with_searchbar()


@index_pages.route("/")
def index():
    listofnewblogs = [[blog.title.capitalize(), blog.content.capitalize(), blog.author] for blog in
                      Blog.query.all()[:3]]

    if current_user.is_anonymous:
        return render_template("index.html", listofnewblogs=listofnewblogs, items=items)

    return render_template("index.html", loggedinuser=current_user.username, is_admin=current_user.is_admin,
                           listofnewblogs=listofnewblogs, items=items)

@index_pages.route("/<int:id>")
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
        # Get for non-login
        return render_template("item.html", **template_args)

    template_args.update({
        'loggedinuser': current_user.username,
        'is_admin': current_user.is_admin
    })

    # Get for login
    return render_template("item.html", **template_args)


@index_pages.route("/<int:id>", methods=["POST"])
def post_item(id):
    return post_with_searchbar()
