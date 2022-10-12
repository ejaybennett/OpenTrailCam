from distutils.log import Log
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_login import LoginManager, login_user, login_required, current_user, UserMixin
import os
from flask_sqlalchemy import SQLAlchemy
from .models import db
from .login import login_manager, register_user, login_correct, app
from .forms import LoginForm, SignupForm
@app.route("/signup", methods = ["GET"])
def signup_page():
    return render_template("signup.html", form = SignupForm())

@app.route("/signup", methods = ["POST"])
def signup():
    if(register_user(request.form["Username"], request.form["Password"], request.form["Email"], request.form["Affiliation"])):
        return redirect(url_for("home"))
    else:
        flash("Wrong username or password!")
    
@app.route("/add_sighting", methods = ["POST"])
def add_sighting():
    pass
        

@app.route("/login", methods = ["GET"])
def login_page():
    return render_template("login.html", form = LoginForm())
@app.route("/login", methods = ["POST"])
def login():
    if(login_correct(request.form)):
        return redirect(url_for("home"))
    else:
        flash("Wrong username or password!")
@app.route("/", methods = ["GET"])
@login_required
def home():
    return "Placeholderrrrr"