from flask import request, redirect, session, Blueprint
import json
import glob
import importlib.util
import os

class Utils(object):

    @staticmethod
    def post_with_searchbar():
        redirect_url = None
        for i in range(2, 5):
            session[f'searchbar_{i}_content'] = request.form[f'searchbar_{i}_content']
            if i == 2:
                redirect_url = session[f'searchbar_{i}_content']
        return redirect(redirect_url)

    @staticmethod
    def read_from_json(file_name):
        with open(file_name, 'r', encoding='utf8') as file:
            data = json.load(file)
            return data

    @staticmethod
    def make_lowercase_plural(word):
        word = word.lower()
        if word.endswith('y'):
            return word[:-1] + 'ies'
        elif word.endswith(('s', 'x', 'z', 'ch', 'sh')):
            return word + 'es'
        else:
            return word + 's'

    @staticmethod
    def delete_keys_from_dict(dictionary, keys_to_delete):
        for key in keys_to_delete:
            dictionary.pop(key, None)

        return dictionary

    @staticmethod
    # Import variables ending with '_pages from files
    def get_blueprints(folder_path='routing/'):
        blueprints = []

        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                if file_name.endswith('.py'):
                    file_path = os.path.join(root, file_name)

                    module_name = os.path.splitext(file_path)[0].replace('/', '.')
                    spec = importlib.util.spec_from_file_location(module_name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # Filter and retrieve variables that are blueprints
                    for var in dir(module):
                        obj = getattr(module, var)
                        if isinstance(obj, Blueprint):
                            setattr(module, var.split('_pages')[0], obj)
                            blueprints.append(obj)

        return blueprints
