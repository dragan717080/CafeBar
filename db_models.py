from datetime import datetime
from config.config import db
from flask_login import UserMixin

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    excluded_keys = ['_sa_instance_state']

    @classmethod
    def remove_excluded_keys(cls, item):
        return {var: value for var, value in vars(item).items() if var not in cls.excluded_keys}

    @classmethod
    def find_all(cls):
        return [cls.remove_excluded_keys(item) for item in cls.query.all()]

    @classmethod
    def find(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_all(cls):
        db.session.query(cls).delete()
        db.session.commit()

    @classmethod
    def delete_one(cls, **kwargs):
        cls.query.filter_by(**kwargs).delete()
        db.session.commit()

    # REST API response
    @classmethod
    def get_latest(cls):
        return cls.remove_excluded_keys(cls.query.order_by(User.created_at.desc()).first())

    def __repr__(self):
        return f'{self.__class__.__name__} {self.id}'

class User(BaseModel, UserMixin):
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default = False)
    excluded_keys = BaseModel.excluded_keys + ['password']

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
