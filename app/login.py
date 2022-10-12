from flask_login import LoginManager, login_user
from .settings import app
from .models import User, db
login_manager = LoginManager()
login_manager.init_app(app)
from werkzeug.security import generate_password_hash, check_password_hash



@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id = id).first()

def login_correct(usernameOrEmail : str, password : str) -> bool:
    user = User.query.filter_by(username=usernameOrEmail).first()
    if user == None:
        user = User.query.filter_by(email=usernameOrEmail).first()
    if user != None and check_password_hash(user.password_hash, password):
        login_user(user)
        return True
    else:
        return False

def register_user(username : str, password : str, email : str, affiliation : str) -> bool:
    username_open = User.query.filter_by(username = username).first() == None
    if not(username_open):
        return False
    user = User(username = username, email = email,
     password_hash = generate_password_hash(password), affiliation = affiliation)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return True
