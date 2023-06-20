from flask import Flask
from flask_login import LoginManager
from config import *
from db_models import *

def create_app():
    app = Flask(__name__, template_folder = 'Templates')

    set_config(app.config, app.jinja_env)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.app_context().push()
    SESSION_TYPE = 'sqlalchemy'
    app.config.from_object(__name__)

    app.config['CORS_HEADERS'] = 'Content-Type'

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app