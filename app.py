import os
import websocket

from flask import Flask, jsonify, Request
# from dependency_injector.wiring import Provide, inject

from adapters.api import initAPI
from configuration.config import ENV_PORT, ENV_DEBUG


app = Flask(__name__)

initAPI(app)

app.run(debug=ENV_DEBUG, port=ENV_PORT, use_reloader=False, threaded=True)



# if __name__ == 'main':
    
