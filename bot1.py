from flask import Flask ,render_template,request
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer 
from chatterbot.trainers import ListTrainer 



app = Flask(__name__)

bot=ChatBot("Kavi")
english_bot =ChatBot("Kavi",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer =ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.hindi")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/aboutus")
def showpage2():
    return render_template("page2.html") 

@app.route("/get")
def get_bot_response():
    userText=request.args.get('msg')
    return str(english_bot.get_response(userText))

if __name__=='__main__':
    app.run()
