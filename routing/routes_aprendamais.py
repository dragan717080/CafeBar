from flask import render_template, Blueprint
from flask_login import current_user
from utils import Utils
from items import items, metodos
from db_models import Blog

aprendamais_pages = Blueprint('aprendamais', __name__,
    template_folder='Templates', static_folder='static', url_prefix = '/')

@aprendamais_pages.route('/aprendamais', methods = ['POST'])
def aprendamais_post():
    return Utils.post_with_searchbar()

@aprendamais_pages.route('/aprendamais')
def aprendamais():
    new_blogs = [[blog.title.capitalize(), blog.content.capitalize(), blog.author] for blog in Blog.query.limit(3).all()]
    template_args = {
        'new_blogs': new_blogs,
        'items': items,
        'metodos': metodos
    }
    if current_user.is_anonymous:
        return render_template('aprendamais.html', **template_args)

    template_args.update({
        'loggedinuser': current_user.username,
        'is_admin': current_user.is_admin
    })

    return render_template('aprendamais.html', **template_args)
