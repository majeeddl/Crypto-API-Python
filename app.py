import os
import json

from flask import Flask
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send, emit
from multiprocessing import Process

from adapters.api import initAPI
from configuration.config import ENV_PORT, ENV_DEBUG


from frameworks.trading_services.trading_websocket_services import TradingWebsocketServices


# def create_app() -> Flask:
#     # app.run(debug=ENV_DEBUG, port=ENV_PORT, use_reloader=False, threaded=True)
#     return app

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
socketio = SocketIO(app, cors_allowed_origins="*")


def connectWs():
    def on_message(ws, message):
        data = json.loads(message)
        emit('data', data)
        print(data)
    print('connectWs')
    tws = TradingWebsocketServices(on_message=on_message)
    tws.start()


@socketio.on('ping')
def handle_message(message):
    print(message['data'])

    # process = Process(target=connectWs)

    # process.start()

    connectWs()

    emit('pong', {'data': 'pong'})


initAPI(app)

# connectWs()

if __name__ == '__main__':
    # app.run(debug=ENV_DEBUG, port=ENV_PORT, use_reloader=False, threaded=True)
    # connectWs()
    socketio.run(app, debug=ENV_DEBUG, port=ENV_PORT,
                 use_reloader=False, threaded=True)
