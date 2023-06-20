from subsidiary_functions import *
from flask_login import current_user
from items import items, metodos
import time

aprendamais_pages = Blueprint('aprendamais', __name__,
                        template_folder='Templates', static_folder='static', url_prefix = "/")

@aprendamais_pages.route("/aprendamais", methods = ["POST"])
def aprendamais_post():
    return post_with_searchbar()

@aprendamais_pages.route("/aprendamais")
def aprendamais():

    listofnewblogs = [[blog.title.capitalize(), blog.content.capitalize(), blog.author] for blog in Blog.query.all()[:3]]

    template_args = {
        'listofnewblogs': listofnewblogs,
        'items': items,
        'metodos': metodos
    }

    if current_user.is_anonymous:
        return render_template("aprendamais.html", **template_args)

    template_args.update({
        'loggedinuser': current_user.username,
        'is_admin': current_user.is_admin
    })

    return render_template("aprendamais.html", **template_args)
