

from flask import Flask,jsonify,Request

app = Flask(__name__)


@app.route("/")
def home():
    return " Hello Flask"