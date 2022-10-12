from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from .settings import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(180), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    affiliation = db.Column(db.String(50))

class Sighting(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id),
        nullable=False)
    species = db.Column(db.String(30), unique=True, nullable=False)
    age = db.Column(db.String(30), nullable = False)
    image = db.Column(db.LargeBinary)
def init_database():
    db.create_all()

def reset_database():
    db.drop_all()
    db.create_all()

