from flask import Blueprint, jsonify
from db_models import User, Blog

api_pages = Blueprint('api', __name__,
    template_folder='Templates', static_folder='static', url_prefix = '/api')

#so far just simple get operations, will refactor sometime in future
@api_pages.route('/users')
def get_all_users():
    return jsonify(User.find_all())

@api_pages.route('/users/<int:user_id>')
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'user_id': user.id, 'username': user.username})

@api_pages.route('/blogs')
def get_all_blogs():
    return jsonify(Blog.find_all())