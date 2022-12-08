

from frameworks.data_services.data_services import DataServices


class UserUseCases:
    def __init__(self) -> None:
        self.dataServices = DataServices()

    def getUsers(self):
        return self.dataServices.users.find()
