import os
import websocket

from flask import Flask
from flask_cors import CORS, cross_origin

from adapters.api import initAPI
from configuration.config import ENV_PORT, ENV_DEBUG


# def create_app() -> Flask:
#     # app.run(debug=ENV_DEBUG, port=ENV_PORT, use_reloader=False, threaded=True)
#     return app

app = Flask(__name__)
cors = CORS(app)

initAPI(app)


if __name__ == '__main__':
    app.run(debug=ENV_DEBUG, port=ENV_PORT, use_reloader=False, threaded=True)
