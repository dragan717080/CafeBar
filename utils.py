from flask import request, redirect, session
import json

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
