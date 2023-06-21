from flask_sqlalchemy import SQLAlchemy

#configuration for the database
db = SQLAlchemy()

#configuration for app
def set_config(app_dict, env):

    #setting app.config
    config_dict = {
        'SECRET_KEY': 'secretkey1',
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///database/users.db',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_BINDS': {
            'users': 'sqlite:///database/users.db',
            'blogs': 'sqlite:///database/blogs.db',
            'items': 'sqlite:///database/items.db'
        },
        'TEMPLATES_AUTO_RELOAD': True,
        'CACHE_TYPE': 'redis',
        'DEFAULT_AVATAR': r"C:\Users\dESKTOP I5\PycharmProjects\UrbeCafeBar\static\images\login-icon.jpg",
        'CORS_HEADERS': 'Content-Type'
    }

    app_dict.update(config_dict)

    # setting jinja_env
    env.auto_reload = True
    env.cache = {}
