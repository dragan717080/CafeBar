from flask_login import UserMixin
from datetime import datetime
from config import db

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    excluded_keys = ['_sa_instance_state', 'id']

    @staticmethod
    def remove_excluded_keys(item):
        return {var: value for var, value in vars(item).items() if var not in BaseModel.excluded_keys}

    @classmethod
    def find_all(cls):
        search_matches = []
        for item in cls.query.all():
            d = cls.remove_excluded_keys(item)
            search_matches.append(d)

        return search_matches

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'{self.__class__.__name__} {self.id}'

class User(BaseModel, UserMixin):
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default = False)
    excluded_keys = BaseModel.excluded_keys + ['password']

    @staticmethod
    def find_all_filter(username):
        search_matches = db.session.query(User).filter_by(username = username).all()
        return search_matches if len(search_matches) > 0 else None

    @staticmethod
    def delete_all():
        db.session.query(User).delete()
        db.session.commit()

    def __repr__(self):
        return f'{self.__class__.__name__} {self.id}'

class Blog(BaseModel, UserMixin):
    __bind_key__ = 'blogs'
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)

class Item(BaseModel):
    __bind_key__ = 'items'
    title = db.Column(db.String, nullable=False)
    pricing = db.Column(db.String, nullable=False)
    imagesource = db.Column(db.String, nullable=False)
