from flask import Flask, render_template
from flask import *

app = Flask(__name__)

b

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/redirect", methods=['POST'])
def dash_page():
    return render_template("dash_page.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/fileUploaded", methods= ['POST'])
def file_load():
    try:
        f = request.files['file']
        f.save(f.filename)
    except FileNotFoundError:
        return redirect('/')
    return render_template("fileu.html", name = f.filename)


if __name__== "__main__":
    app.run(debug=True)

