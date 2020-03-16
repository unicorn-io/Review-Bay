from flask import Flask, render_template
from flask import *
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer 
from chatterbot.trainers import ListTrainer 


app = Flask(__name__)
bot=ChatBot("Ravi")
train_bot =ChatBot("Ravi",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer =ChatterBotCorpusTrainer(train_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.hindi")
trainer.train('train.yml')




@app.route('/')
def index():
    return render_template("index.html")

@app.route("/submit")
def dash_page():
    pass

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
    app.run()

