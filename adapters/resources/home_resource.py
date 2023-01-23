from flask import jsonify
from flask_restful import Resource

from use_cases.user.users_useCase import UserUseCases



class HomeResource(Resource):

    def __init__(self) -> None:
        self.userUseCase = UserUseCases()
        super().__init__()

    def get(self):
        print(self.userUseCase.getUsers())
        return jsonify({"message": "hello world"})

    def post(self):
        return jsonify({"message": "post data"})


# Hi
