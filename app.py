from flask import Flask
from flask_cors import CORS
import os
import nltk


app = Flask(__name__)
CORS(app)

from routes.msg import *

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)




    
