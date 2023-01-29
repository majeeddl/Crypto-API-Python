# from time import sleep
# from pybit import usdt_perpetual
# ws_linear = usdt_perpetual.WebSocket(
#     test=True,
#     ping_interval=30,  # the default is 30
#     ping_timeout=10,  # the default is 10
#     domain="bybit"  # the default is "bybit"
# )


# def handle_message(msg):
#     print(type(msg))
#     print(msg)
#     print(msg['data'][0]['price'])
#     print("***************")


# # To subscribe to multiple symbols,
# # pass a list: ["BTCUSDT", "ETHUSDT"]
# ws_linear.trade_stream(
#     handle_message, "EOSUSDT"
# )
# while True:
#     sleep(1)


from time import sleep
from pybit import usdt_perpetual
ws_linear = usdt_perpetual.WebSocket(
    test=True,
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)


def handle_message(msg):
    print(msg)


# To subscribe to multiple symbols,
# pass a list: ["BTCUSDT", "ETHUSDT"]

# pass an interval
ws_linear.trade_stream(
    handle_message, "APETUSDT"
)
while True:
    sleep(1)

# How can I connect to bybit web socket in python?


# # import the necessary libraries
# import websocket
# import json

# # define the websocket URL
# url = "wss://stream.bybit.com/realtime"

# # open the websocket connection
# ws = websocket.create_connection(url)

# # send a subscription request to the server
# subscribe_request = {
#     "op": "subscribe",
#     # subscribing to BTCUSD instrument info updates every 100ms
#     "args": ["trade.BTCUSDT"]
# }
# ws.send(json.dumps(subscribe_request))

# # receive data from the server and print it out on the console
# while True:
#     response = ws.recv()  # receive data from server

#     print(response)
