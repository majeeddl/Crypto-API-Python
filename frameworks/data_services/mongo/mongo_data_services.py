

from domain.abstracts.data_service_abstract import DataServicesAbstract
from frameworks.data_services.mongo.repository.exchange_repository import ExchangeRepository
from frameworks.data_services.mongo.repository.user_repository import UserRepository


class MongoDataServices(DataServicesAbstract):

    # users: UserRepository

    # def __init__(self) -> None:
    #     # self.users = UserRepository()
    #     pass

    @property
    def users(self):
        return UserRepository()

    @property
    def exchanges(self):
        return ExchangeRepository()
