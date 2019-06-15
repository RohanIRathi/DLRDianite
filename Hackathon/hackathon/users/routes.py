from flask import render_template, url_for, flash, redirect, request, Blueprint
from hackathon.users.forms import RegistrationForm
from hackathon.models import User
from hackathon import db

users = Blueprint('users',__name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash('Your name has been recorded', 'success')
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)