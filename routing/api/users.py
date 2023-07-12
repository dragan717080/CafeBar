from flask import Blueprint, jsonify, request
from db_models import User, Blog
import traceback

api_users_pages = Blueprint('api_users', __name__, url_prefix = '/api/users/')

@api_users_pages.route('/')
def get_all_users():
    return jsonify(User.find_all())

@api_users_pages.route('/<int:id>')
def get_user(id):
    user = User.find(id=id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(User.remove_excluded_keys(user))

@api_users_pages.route('/', methods=['POST'])
def create_user():
    data = request.get_json()

    try:
        user_dict = {
            'email': data['email'],
            'username': data['username'],
            'password': data['password'],
            'is_admin': True if 'is_admin' in data else False
        }

        user = User(**user_dict)
        user.save()

        return jsonify(User.get_latest()), 201

    except Exception as e:
        traceback_str = traceback.format_exc()

        return jsonify({'error': 'An exception occurred', 'traceback': traceback_str}), 500

@api_users_pages.route('/<int:id>', methods=['PATCH'])
def update_user(id):
    user = User.find(id=id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()

    try:
        # Update the user attributes based on the provided data
        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)

        user.save()

        return jsonify(User.remove_excluded_keys(user))

    except Exception as e:
        return jsonify({'error': 'Invalid parameters'}), 406

@api_users_pages.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.find(id=id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    try:
        User.delete_one(id=id)

        return jsonify({'message': 'User deleted'})

    except Exception as e:
        traceback_str = traceback.format_exc()
        return jsonify({'error': 'An exception occurred', 'traceback': traceback_str}), 500
