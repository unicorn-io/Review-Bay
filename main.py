from flask import Blueprint
from . import db
from flask import render_template
from flask import redirect
from flask import request
from flask import Response
from flask_login import login_required, current_user
from flask import send_file
from .analyse import *
from .row_gen import generate_table, get_list
import pandas as pd
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
#from .sent_model import gen_file

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
    #gen_file('./data_infi.csv')
    data = pd.read_csv('./SIH/a.csv')
    return render_template("dash_page.html", num_products=get_prod_count(data),
     num_good=get_good_count(data),good_percent=get_good_percent(data),
      num_neutral=get_neutral_count(data), neutral_percent=get_neutral_percent(data),
        num_bad=get_bad_count(data), bad_percent=get_bad_percent(data))

@main.route("/dynamicView")
@login_required
def dyn_view():
    data = pd.read_csv('a.csv')
    listo = data.values.tolist()
    generate_table(listo)
    foo = open('./SIH/table.txt', 'r')
    return render_template('dynamic_view.html', table_data=foo.read())


@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/fileUploaded", methods= ['POST'])
@login_required
def file_load():
    try:
        f = request.files['filey']
        if (f.filename == ''): return redirect('/redirect')
        f.save('data_infi.csv')
        
    except:
        return redirect('/')
    return render_template("fileu.html", name = f.filename)

@main.route("/downloadResults", methods=['GET', 'POST'])
def file_download():
    return send_file('./a.csv', as_attachment=True)
    

@main.route("/goodPreds")
@login_required
def good_csv():
    good_list = []
    lis = get_list()
    for l in lis:
        try:
            if (l[3] == '1'):
                good_list.append(l)
        except:
            continue
    generate_table(good_list)
    f = open('./SIH/table.txt', 'r')
    return render_template('dynamic_view.html',   table_data=f.read(), len_reviews=len(good_list))

@main.route("/badPreds")
@login_required
def bad_csv():
    listo = []
    lis = get_list()
    for l in lis:
        try:
            if (l[4] == '1'):
                listo.append(l)
        except:
            continue
    generate_table(listo)
    f = open('./SIH/table.txt', 'r')
    return render_template('dynamic_view.html',   table_data=f.read(), len_reviews=len(listo))

@main.route("/neutralPreds")
@login_required
def neutral_csv():
    listo = []
    lis = get_list()
    for l in lis:
        try:
            if (l[5] == '1'):
                listo.append(l)
        except:
            continue
    generate_table(listo)
    f = open('./SIH/table.txt', 'r')
    return render_template('dynamic_view.html',   table_data=f.read(), len_reviews=len(listo))

@main.route("/searchQuery", methods= ['POST'])
@login_required
def query_csv():
    query = request.form['search_query'].split(" ")
    print(query)
    data = pd.read_csv('./SIH/a.csv')
    lis= data.values.tolist()
    listo = []
    for l in lis:
        try:
            key = [a.lower() for a in l[1].split(" ")]
            key = [a for a in query if a in key]
            if (l[0].lower() == query[0].lower() or len(key) > 0):
              listo.append(l)
              
        except:
            continue
    generate_table(listo)
    foo = open('./SIH/table.txt', 'r')
    return render_template('dynamic_view.html', table_data=foo.read(), len_reviews=len(listo))    

@main.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig