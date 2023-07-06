from flask import request, redirect, session
import json
import glob
import importlib.util

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
        file_paths = glob.glob(folder_path + '*.py')

        blueprints = []
        for file_path in file_paths:
            file_name = file_path[:-3].split('/')[-1]  # Extract the file name without the '.py' extension
            module_name = file_name.replace('.', '_')  # Convert the file name to a valid module name
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Filter and retrieve variables that end with '_pages'
            blueprints.append([getattr(module, var) for var in dir(module) if var.endswith('_pages')][0])
        return blueprints
