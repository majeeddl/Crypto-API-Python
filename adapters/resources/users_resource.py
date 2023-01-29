from flask import jsonify
from flask_restful import Resource

from use_cases.user.users_useCase import UserUseCases




class UsersResource(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.userUseCase = UserUseCases()

    def get(self):
        return jsonify(self.userUseCase.getUsers())

    def post(self):
        return jsonify({"message": "post data"})
