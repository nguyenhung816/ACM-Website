from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import SignupForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup' , methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash('You have successfully signed up!')
        return redirect(url_for('index', _anchor="content"))
    return render_template('signup.html', form=form)
