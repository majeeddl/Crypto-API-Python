from time import sleep
from pybit import usdt_perpetual
ws_linear = usdt_perpetual.WebSocket(
    test=True,
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)


def handle_message(msg):
    print(type(msg))
    print(msg)
    print(msg['data'][0]['price'])
    print("***************")


# To subscribe to multiple symbols,
# pass a list: ["BTCUSDT", "ETHUSDT"]

ws_linear.trade_stream(
    handle_message, "APETUSDT"
)
while True:
    sleep(1)
