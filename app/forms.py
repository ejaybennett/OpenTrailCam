from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
class LoginForm(FlaskForm):
    usernameOrEmail = StringField(name="Username Or Email",  validators= [DataRequired(), Length(3, 20)])
    password = StringField(name="Password",  validators= [DataRequired(), Length(3, 20)])

class SignupForm(FlaskForm):
    username = StringField(name="Username",  validators= [DataRequired(), Length(3, 20)])
    password = StringField(name="Password",  validators= [DataRequired(), Length(3, 20)])
    affiliation= StringField(name="Affiliation",  validators= [DataRequired(), Length(3, 20)])
    email = StringField(name="Email",  validators= [DataRequired(), Length(3, 20)])