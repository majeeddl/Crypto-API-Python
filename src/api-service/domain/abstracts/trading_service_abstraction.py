
from abc import ABC, abstractmethod, abstractproperty

from frameworks.trading_services.trading_positions_services import TradingPositionServices


class TradingServiceAbstract(ABC):

    @property
    @abstractmethod
    def positions() -> TradingPositionServices:
        '''positions'''
        pass

    @property
    @abstractmethod
    def orders():
        '''positions'''
        pass
