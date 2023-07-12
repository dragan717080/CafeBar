from flask import Blueprint, jsonify
from db_models import User, Blog

api_blogs_pages = Blueprint('api_blogs', __name__, url_prefix = '/api/blogs/')

#so far just simple get operations, will refactor sometime in future
@api_blogs_pages.route('/')
def get_all_blogs():
    return jsonify(Blog.find_all())

@api_blogs_pages.route('/<int:blog_id>')
def get_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog is None:
        return jsonify({'error': 'Blog not found'}), 404

    return jsonify({'blog_id': blog.id, 'title': blog.title})
