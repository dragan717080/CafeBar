from flask_sqlalchemy import SQLAlchemy

#configuration for the database
db = SQLAlchemy()

#configuration for app
def set_config(dict, env):
    #setting app.config
    dict['SECRET_KEY'] = 'secretkey1'
    dict['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
    dict['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    dict['SQLALCHEMY_BINDS'] = {"users": "sqlite:///users.db", "blogs": "sqlite:///blogs.db", "items": "sqlite:///items.db"}
    dict['TEMPLATES_AUTO_RELOAD'] = True
    dict["CACHE_TYPE"] = "redis"
    dict['DEFAULT_AVATAR'] = "C:\\Users\dESKTOP I5\PycharmProjects\\UrbeCafeBar\\static\\images\\login-icon.jpg"
    dict['CORS_HEADERS'] = 'Content-Type'

    # setting jinja_env
    env.auto_reload = True
    env.cache = {}

