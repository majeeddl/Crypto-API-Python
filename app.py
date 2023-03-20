import os
import json

from flask import Flask
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send, emit

from adapters.api import initAPI
from configuration.config import ENV_PORT, ENV_DEBUG


from frameworks.trading_services.trading_websocket_services import TradingWebsocketServices


# def create_app() -> Flask:
#     # app.run(debug=ENV_DEBUG, port=ENV_PORT, use_reloader=False, threaded=True)
#     return app

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
socketio = SocketIO(app, cors_allowed_origins="*", message_queue='redis://')


@socketio.on('ping')
def handle_message(message):
    print(message['data'])

    # def on_message(message):
    #     data = json.loads(message)
    #     print(data)

    # tws = TradingWebsocketServices()

    # tws.start()

    emit('pong', {'data': 'pong'})


initAPI(app)

if __name__ == '__main__':
    # app.run(debug=ENV_DEBUG, port=ENV_PORT, use_reloader=False, threaded=True)

    socketio.run(app, debug=ENV_DEBUG, port=ENV_PORT,
                 use_reloader=False, threaded=True)
