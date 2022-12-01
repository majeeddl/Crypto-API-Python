import os
import websocket

from flask import Flask,jsonify,Request
from flask_restful import Api
from adapters.resources.telegram_resource import TelegramReource

from configuration.config import ENV_PORT,ENV_DEBUG
from adapters.resources.home_resource import HomeResource
from frameworks.telegram_services.telergram_service import run_telegram_service

app = Flask(__name__)

api = Api(app)

api.add_resource(HomeResource,"/")
# api.add_resource(TelegramReource,"/telegram")



if __name__ == 'main' :
    app.run(debug=ENV_DEBUG,port=ENV_PORT,use_reloader=False,threaded=True)
