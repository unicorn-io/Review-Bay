# auth.py

from flask import Blueprint
from . import db
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from .models import User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup', methods=['POST'])
def signup():
    return redirect('/')

def signup_post():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('pwd')
    mobile_number = request.form.get('mob')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash("email already exists")
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), mobile_number=mobile_number)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'