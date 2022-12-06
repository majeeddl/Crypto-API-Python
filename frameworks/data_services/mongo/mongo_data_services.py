


from domain.entities.user_entity import User
from frameworks.data_services.mongo.repository.mongo_repository import MongoRepository


class MongoDataServices:

    def __init__(self) -> None:

        self.users = MongoRepository[User]
        pass

    # def users():
    #     return self