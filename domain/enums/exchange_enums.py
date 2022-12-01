
from enum import Enum

class ExchangeTypeEnum(Enum):
    def __str__(self):
        return str(self.name)

    binance=1
    kucoin=2
    bybit=3
