

from domain.abstracts.data_service_abstract import DataServicesAbstract
from frameworks.data_services.mongo.repository.user_repository import UserRepository


class MongoDataServices(DataServicesAbstract):

    # users: UserRepository

    # def __init__(self) -> None:
    #     # self.users = UserRepository()
    #     pass

    @property
    def users(self):
        return UserRepository()

    # def exchanges(self):
    #     return []
