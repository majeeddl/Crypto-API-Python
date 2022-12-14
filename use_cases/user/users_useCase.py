

from domain.entities.user_entity import User
from frameworks.data_services.data_services import DataServices


class UserUseCases:

    def __init__(self) -> None:
        self.dataServices = DataServices()

    def getUsers(self) -> list(User):
        return self.dataServices.users.find()

    def getUserById(self,id:str) -> User:
        return self.dataServices.users.findById(id)

    def createUser(self,newUser: User) -> User:
        return self.dataServices.users.create(newUser)

    def updateUser(self, updatedUser: User):
        return self.dataServices.users.update(updatedUser)

    def deleteUser(self, id:str) -> None:
        return self.dataServices.users.delete(id);
