# main.py

from flask import Blueprint
from . import db
from flask import render_template
from flask import redirect
from flask import request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route("/redirect", methods=['POST'])
def dash_page():
    return render_template("dash_page.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/fileUploaded", methods= ['POST'])
def file_load():
    try:
        f = request.files['file']
        f.save(f.filename)
    except FileNotFoundError:
        return redirect('/')
    return render_template("fileu.html", name = f.filename)

