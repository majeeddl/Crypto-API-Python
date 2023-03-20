
import os
from domain.entities.exchange_entity import Exchange, ExchangeConfig
from frameworks.trading_services.trading_services import TradingServices


class TradingUseCases:

    def __init__(self) -> None:

        API_KEY = os.environ.get('BYBIT_API')
        API_SECRET = os.environ.get('BYBIT_SECRET')

        self.exchange = Exchange(name='bybit', config=ExchangeConfig(
            api_key=API_KEY, api_secret=API_SECRET))

        print(self.exchange)

        self.tradingServices = TradingServices(exchange=self.exchange)

    def fetch_positions(self):
        return self.tradingServices.positions().fetch()
