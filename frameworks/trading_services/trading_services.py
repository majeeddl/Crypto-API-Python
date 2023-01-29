

import ccxt
from domain.abstracts.trading_service_abstraction import TradingServiceAbstract
from domain.entities.exchange_entity import Exchange
from frameworks.trading_services.trading_positions_services import TradingPositionServices


class TradingServices(TradingServiceAbstract):

    def __init__(self, exchange: Exchange) -> None:
        self.exchange = exchange

    def positions(self) -> TradingPositionServices:
        return TradingPositionServices(self.exchange)

    def orders():
        pass
