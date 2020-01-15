# auth.py

from flask import Blueprint
from . import db
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from flask_login import login_user, logout_user, login_required
from .models import User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET","POST"])
def login_post():
    email = request.form.get('email1')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect('/') # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect('/redirect')

@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('pwd')
    mobile_number = request.form.get('mob')
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash("email already exists")

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), mobile_number=mobile_number)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login_post'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))