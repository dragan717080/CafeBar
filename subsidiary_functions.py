from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash, Blueprint
from config import *
from db_models import *
from log_config import logging
from create_app import create_app
import json

app = create_app()

def post_with_searchbar():

    redirect_url = None
    for i in range(2, 5):
        session[f'searchbar_{i}_content'] = request.form[f'searchbar_{i}_content']
        if i == 2:
            redirect_url = session[f'searchbar_{i}_content']
    return redirect(redirect_url)

def read_from_json(file_name):
    with open(file_name) as file:
        data = json.load(file)
        return data

#generate file names for db models e.g. Blog to blogs
def make_lowercase_plural(word):
    word = word.lower()
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return word + 'es'
    else:
        return word + 's'

print(make_lowercase_plural('Blog'))