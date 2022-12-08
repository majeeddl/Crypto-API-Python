import os
import websocket

from flask import Flask

from adapters.api import initAPI
from configuration.config import ENV_PORT, ENV_DEBUG


# def create_app() -> Flask:


#     # test()

#     # app.run(debug=ENV_DEBUG, port=ENV_PORT, use_reloader=False, threaded=True)

#     return app

app = Flask(__name__)

initAPI(app)

app.run(debug=ENV_DEBUG, port=ENV_PORT, use_reloader=False, threaded=True)
