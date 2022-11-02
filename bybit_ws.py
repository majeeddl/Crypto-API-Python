"""
To see which endpoints and topics are available, check the Bybit API 
documentation: https://bybit-exchange.github.io/docs/inverse/#t-websocket
There are several WSS URLs offered by Bybit, which pybit manages for you.
However, you can set a custom `domain` as shown below.
"""

import logging
from time import sleep

# Import your desired markets from pybit
from pybit import inverse_perpetual
from pybit import spot

"""
An alternative way to import:
from pybit.inverse_perpetual import WebSocket, HTTP
"""

# Set up logging (optional)
logging.basicConfig(filename="pybit.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")


# Connect with authentication!
ws_inverse = inverse_perpetual.WebSocket(
    # test=True,
    api_key="...",  # omit the api_key & secret to connect w/o authentication
    api_secret="...",
    # to pass a custom domain in case of connectivity problems, you can use:
    domain="bytick"  # the default is "bybit"
)

# Let's fetch the orderbook for BTCUSD. First, we'll define a function.


def handle_orderbook(message):
    # I will be called every time there is new orderbook data!
    print(message)
    orderbook_data = message["data"]


# Now, we can subscribe to the orderbook stream and pass our arguments:
# our function and our selected symbol.
# To subscribe to multiple symbols, pass a list: ["BTCUSD", "ETHUSD"]
# To subscribe to all symbols, pass "*".
ws_inverse.orderbook_25_stream(handle_orderbook, "BTCUSD")


# To subscribe to private data, the process is the same:
def handle_position(message):
    # I will be called every time there is new position data!
    print(message)


ws_inverse.position_stream(handle_position)


# Similarly, if you want to listen to the WebSockets of other markets:
ws_spot = spot.WebSocket(test=True)
# handle_orderbook() will now be called for both inverse and spot data.
# To keep the data separate, simply create another function and pass it below.
ws_spot.depth_v2_stream(handle_orderbook, "BTCUSDT")


while True:
    # This while loop is required for the program to run. You may execute
    # additional code for your trading logic here.
    sleep(1)
