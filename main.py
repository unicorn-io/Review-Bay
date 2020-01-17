# main.py

from flask import Blueprint
from . import db
from flask import render_template
from flask import redirect
from flask import request
from flask_login import login_required, current_user
from flask import send_file
from .analyse import *

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route("/redirect", methods=['GET','POST'])
@login_required
def redirected():
    return render_template("login.html")

@main.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dash():
    return render_template("dash_page.html", num_products=get_prod_count(),
     num_good=get_good_count(),good_percent=get_good_percent(),
      num_neutral=get_neutral_count(), neutral_percent=get_neutral_percent(),
        num_bad=get_bad_count(), bad_percent=get_bad_percent())

@main.route("/dynamicView")
@login_required
def dyn_view():
    return render_template('dynamic_view.html')

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/fileUploaded", methods= ['POST'])
@login_required
def file_load():
    try:
        f = request.files['filey']
        if (f.filename == ''): return redirect('/redirect')
        f.save(f.filename)
        
    except:
        return redirect('/')
    return render_template("fileu.html", name = f.filename)

@main.route("/downloadResults", methods=['GET', 'POST'])
def file_download():
    return send_file('./a.csv', as_attachment=True)
    