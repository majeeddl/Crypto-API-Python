
import ccxt


from domain.abstracts.exchange_service_abstract import ExchangeServiceAbstract
from domain.enums.exchange_enums import ExchangeTypeEnum


class ExchangeServices(ExchangeServiceAbstract):

    def __init__(self) -> None:
        exchange_id = ExchangeTypeEnum.bybit
        exchange_class = getattr(ccxt, exchange_id)
        exchange = exchange_class()
        exchange.enableRateLimit = True
        exchange.options = { }
        print(exchange_id)
        print(exchange_class)
        m = exchange.fetchTickers()
        print(m)
        pass

    def fetchAccounts():
        pass

    def fetchBalance():
        pass
