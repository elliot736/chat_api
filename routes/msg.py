from flask import Flask
from flask import request
# from services.answerMsgBert import answerMsgBert
from controllers.pipeline import pipeline
from controllers.translate import translate2en, translate2de
from services.spellcorrection import SpellCorrection

from app import app
@app.route("/")
def index():
    return "Hello, World!"
    
@app.route("/sendMsg", methods=["POST"])
def send_main():
    msg= request.args.get("msg")
    msg = SpellCorrection(msg)
    answer = pipeline(msg)
    return answer

@app.route("/translate2en", methods=["POST"])
def send():
    msg= request.args.get("msg")
    answer = translate2en(msg)
    return answer

@app.route("/translate2de", methods=["POST"])
def send_de():
    msg= request.args.get("msg")
    answer = translate2de(msg)
    return answer



#http://127.0.0.1:8080/sendMsg?msg=i'm unable to access any of my data or programs on my computer

