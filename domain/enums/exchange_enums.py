
from enum import Enum

class ExchangeTypeEnum(str,Enum):
    # def __str__(self):
    #     return str(self.name)

    binance='binance'
    bybit = 'bybit'
    kucoin='kucoin'
    
