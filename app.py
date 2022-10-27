import os

from flask import Flask,jsonify,Request
from flask_restful import Api

from adapters.resources.home import HomeApi

app = Flask(__name__)

api = Api(app)

# @app.route("/")
# def home():
#     return " Hello Flask"

api.add_resource(HomeApi,"/")


if __name__ == 'main' :
    ENV_DEBUG=os.getenv("DEBUG",True)
    ENV_PORT=os.getenv("PORT",5000)
    app.run(debug=ENV_DEBUG,port=ENV_PORT,use_reloader=True)
