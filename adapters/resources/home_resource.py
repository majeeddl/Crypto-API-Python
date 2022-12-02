from flask import jsonify
from flask_restful import Resource
from dependency_injector.wiring import Provide, inject


from configuration.config import Config
from containers import Container
from services import SearchService

# from use_cases.user.users_useCase import UserUseCases


class HomeResource(Resource):

    # def __init__(self) -> None:
    #     super().__init__()

    # @inject
    # def __init__(self, userUseCases: UserUseCases = Provide[Containers.useCases.userUseCase]) -> None:
    #     self.users = userUseCases
    #     print(self.users.getUsers())
    #     super().__init__()

    def __init__(self) -> None:
        super().__init__()

    @inject
    def get(self, search_service: SearchService = Provide[Container.search_service]):

        print(search_service.repositories())
        print("test")
        return jsonify({"message": "hello world"})

    def post(self):
        return jsonify({"message": "post data"})
