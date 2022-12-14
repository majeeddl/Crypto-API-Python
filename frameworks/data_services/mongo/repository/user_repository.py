

from frameworks.data_services.mongo.repository.mongo_repository import MongoRepository
from domain.entities.user_entity import User

class UserRepository(MongoRepository[User]) :
    def __init__(self) -> None:
        super().__init__('users')