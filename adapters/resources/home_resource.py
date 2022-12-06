from flask import jsonify
from flask_restful import Resource
from dependency_injector.wiring import Provide, inject


# from configuration.config import Config
from containers import Container
from use_cases.user.users_useCase import UserUseCases


# @inject
# def test(userUseCases: UserUseCases = Provide[Container.useCases.userUseCase]):
#     print(userUseCases.getUsers())


class HomeResource(Resource):

    def __init__(self) -> None:

        super().__init__()

    def get(self):
        self.userUseCases.getUsers()
        return jsonify({"message": "hello world"})

    def post(self):
        return jsonify({"message": "post data"})
