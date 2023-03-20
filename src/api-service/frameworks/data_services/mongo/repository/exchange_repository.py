

from domain.entities.exchange_entity import Exchange
from frameworks.data_services.mongo.repository.mongo_repository import MongoRepository


class ExchangeRepository(MongoRepository[Exchange]):

    def __init__(self) -> None:
        super().__init__('exchanges')
