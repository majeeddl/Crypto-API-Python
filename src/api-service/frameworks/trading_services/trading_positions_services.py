

import ccxt

class TradingPositionServices():

    def __init__(self,exchange) -> None:
        self.exchange = exchange;
        self.ccxt_exchange = ccxt.bybit({
            'apiKey': exchange.config.api_key,
            'secret': exchange.config.api_secret,
            'enableRateLimit': True,
            'options': {
                'defaultType': 'future',
                'adjustForTimeDifference': True
            },
            'verbose': False,
        })

        pass

    def fetch(self):
        return self.ccxt_exchange.fetch_positions()
