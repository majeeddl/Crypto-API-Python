import json
import logging
import time
from datetime import datetime
import websocket

topic = "kline.5.COCOSUSDT"


def on_message(ws, message):
    print('base on_message => message received')
    data = json.loads(message)
    print(data)


def on_error(ws, error):
    print('we got error')
    print(error)
    print('print error complete')


def on_close(ws):
    print("### about to close please don't close ###")


def on_open(ws):
    print('opened')
    ws.send(json.dumps({"op": "subscribe", "args": [topic]}))


def on_pong(ws, *data):
    print('pong received')


def on_ping(ws, *data):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    print('ping received')


class TradingWebsocketServices():

    def __init__(self, topic="kline.5.BTCUSDT", on_message=on_message):
        print('init TradingWebsocketServices')
        # websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            # "wss://stream.bybit.com/contract/usdt/public/v3",
            "wss://stream.bybit.com/v5/public/linear",
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
            on_ping=on_ping,
            on_pong=on_pong,
            on_open=on_open
        )
        pass

    def connWS(self):
        pass

    def start(self):
        print('start TradingWebsocketServices')
        self.ws.run_forever(
            ping_interval=20,
            ping_timeout=10
        )

    def stop(self):
        self.ws.close()
