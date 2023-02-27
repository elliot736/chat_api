from flask import Flask
from flask import request
# from services.answerMsgBert import answerMsgBert
from controllers.pipeline import pipeline
from controllers.translate import translate
from app import app
@app.route("/")
def index():
    return "Hello, World!"
    
@app.route("/sendMsg", methods=["POST"])
def send_main():
    msg= request.args.get("msg")
    answer = pipeline(msg)
    return answer

@app.route("/translate", methods=["POST"])
def send():
    msg= request.args.get("msg")
    answer = translate(msg)
    return answer

# @app.route("/bert/sendMsg", methods=["POST"])
# def send():
#     msg= request.args.get("msg")
#     answer = answerMsgBert(msg)
#     return answer

# @app.route("/svm/sendMsg", methods=["POST"])
# def send2():
#     msg= request.args.get("msg")
#     answer = answerMsgBert(msg)
#     return answer

#http://127.0.0.1:5000/sendMsg?msg=i'm unable to access any of my data or programs on my computer

