from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from datetime import datetime
from app.models import UserPassword

class SignupForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()], render_kw={"placeholder": "First name", "class": "login-item", "id": "firstName"})
    last_name = StringField('Last name', validators=[DataRequired()], render_kw={"placeholder": "Last name", "class": "login-item", "id": "lastName"})
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "Email", "class": "login-item", "id": "email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password", "class": "login-item", "id": "password"})

    submit = SubmitField('Sign-Up')


    def validate_email(self, email):
        user = UserPassword.query.filter_by(email=email.data).first()
        #check if email is already in database
        if user is not None:
            raise ValidationError('You already have an account. Please log in.')
        #check if email is already in ends in uhd.edu
        if not email.data.endswith('gator.uhd.edu'):
            raise ('Please use a gator email address')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "Login Email", "class": "login-item"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password", "class": "login-item"})
    submit = SubmitField('Log in')




    def __repr__(self):
        return '<User {}>'.format(self.email)





