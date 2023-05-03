

from domain.entities.exchange_entity import Exchange
from frameworks.data_services.data_services import DataServices


class ExchangeUseCases:

    def __init__(self) -> None:
        self.dataServices = DataServices()

    def getExchanges(self):
        return self.dataServices.exchanges.find()

    def getExchangeById(self,id:str):
        return self.dataServices.exchanges.findById(id)

    def createExchange(self, exchange:Exchange):
        return self.dataServices.exchanges.create(exchange)

    def update_exchange(self, exchange:Exchange):
        return self.dataServices.exchanges.update(exchange)
