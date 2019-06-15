from flask import render_template, url_for, flash, redirect, request
from hackathon import app, db
from hackathon.forms import RegistrationForm
from hackathon.models import User
from flask_login import current_user


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Your Name Has Been Verfied!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
