

from time import sleep
from pybit import usdt_perpetual, inverse_futures, inverse_perpetual

# symbol_list = ["BTCUSDT", "ETHUSDT"]
symbol_list = ["COCOSUSDT"]

ws_linear = usdt_perpetual.WebSocket(
    test=False,
    ping_interval=30,  # the default is 30
    ping_timeout=10,  # the default is 10
    domain="bybit"  # the default is "bybit"
)


def handle_message(msg):
    # print(msg)
    data = msg['data'][0]
    symbol = msg['topic'][9:]
    price = data['close']
    print(f"Symbol: {symbol}   Price: {price}")


# pass an interval
ws_linear.kline_stream(
    handle_message, symbol_list, "5"
)
while True:
    sleep(1)

