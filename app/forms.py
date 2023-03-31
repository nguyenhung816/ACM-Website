from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from app.database import db

class SignupForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()], render_kw={"placeholder": "First name", "class": "login-item"})
    last_name = StringField('Last name', validators=[DataRequired()], render_kw={"placeholder": "Last name", "class": "login-item"})
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "Email", "class": "login-item"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password", "class": "login-item"})
    submit = SubmitField('Sign-Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "Login Email", "class": "login-item"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password", "class": "login-item"})
    submit = SubmitField('Log in')




    def __repr__(self):
        return '<User {}>'.format(self.email)





