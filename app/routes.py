from app import app
from flask import render_template, flash, redirect, url_for, jsonify, Response, json
from app.forms import SignupForm, LoginForm

from app import db
from app.models import User, UserPassword

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    print(form.data)
    if form.validate_on_submit():
        # create a new user instance
        #validate_csrf(form.csrf_token.data)
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
        )
        # add the user to the database
        db.session.add(new_user)
        db.session.commit()

        # save the password in the UserPassword table
        new_password = UserPassword(
            email=form.email.data,
            password=form.password.data,
            user=new_user
        )
        db.session.add(new_password)
        db.session.commit()

        # flash a success message and redirect to index page
        flash('You have successfully signed up!')
        #response = Response(response=json.dumps({'message': 'User created successfully', 'user': {'username': new_user.first_name, 'email': new_user.email, 'id': new_user.id}}), status=201, mimetype='application/json')
        #return response
        return render_template('index.html', form=form)
    else:
        return render_template('signup.html', form=form)
    return jsonify({'message': 'Failed to register'})

    


