from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .secrets import SECRET_KEY
app = Flask(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://postgres:postgres@localhost:5432/opentrails'
db = SQLAlchemy(app)