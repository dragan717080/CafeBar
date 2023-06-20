from subsidiary_functions import *
from flask_login import current_user
from log_config import logging
import time

blogs_pages = Blueprint('blogs', __name__,
                        template_folder='Templates', static_folder='static', url_prefix = "/")

@blogs_pages.route("/blogs", methods=["POST"])
def blogs_post():

    blog_title = request.form['title']
    blog_content = request.form['content']
    blog_author = current_user.username
    blog_datetime = datetime.utcnow()
    x = datetime(blog_datetime.year, blog_datetime.month, blog_datetime.day, blog_datetime.hour,
                 blog_datetime.minute, blog_datetime.second)
    logging.debug(x)
    new_blog = Blog(title=blog_title, content=blog_content, author=blog_author, datetime=x)
    db.session.add(new_blog)
    db.session.commit()

    return redirect("/blogs")

@blogs_pages.route("/blogs", methods = ["GET"])
def blogs():

    all_blogs = Blog.query.order_by(Blog.datetime).all()
    all_blogs.reverse()
    loggedinuser = current_user.username
    return render_template("blogs.html", loggedinuser = loggedinuser, blogs=all_blogs, author = current_user.username)

@blogs_pages.route("/blogs/delete/<int:id>")
def delete(id):

    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect("/blogs")

@blogs_pages.route("/edit/<int:id>", methods = ["GET", "POST"])
def edit(id):

    blog = Blog.query.get_or_404(id)
    if request.method == "POST":

        blog.title = request.form['title']
        blog.content = request.form['content']
        blog.author = current_user.username
        db.session.commit()

        return redirect("/blogs")
    else:
        return render_template("edit.html", blog = blog)