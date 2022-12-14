

from domain.entities.user_entity import User
from frameworks.data_services.data_services import DataServices


class UserUseCases:

    def __init__(self) -> None:
        self.dataServices = DataServices()

    def getUsers(self):
        return self.dataServices.users.find()

    def getUserById(self,id:str):
        return self.dataServices.users.findById(id)

    def create(self,user:User):
        return self.dataServices.users.create(user)