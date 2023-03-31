from app import app
from flask import render_template, flash, redirect, url_for, jsonify, Response, json
from app.forms import SignupForm, LoginForm

from app import db
from app.models import  UserPassword, UserAccount

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # create a new user instance
        new_user = UserAccount(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data
        )
        # add the user to the database
        db.session.add(new_user)
        db.session.commit()

        # save the password in the UserPassword table
        new_password = UserPassword(
            email=form.email.data,
            password=form.password.data,
            user_account_id=new_user.id
        )
        db.session.add(new_password)
        db.session.commit()


        # flash a success message and redirect to index page
        flash('You have successfully signed up!')
        return render_template('index.html', form=form)
    else:
        return render_template('signup.html', form=form)


    


