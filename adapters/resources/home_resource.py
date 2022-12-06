from flask import jsonify
from flask_restful import Resource
from dependency_injector.wiring import Provide, inject


from configuration.config import Config


class HomeResource(Resource):

    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return jsonify({"message": "hello world"})

    def post(self):
        return jsonify({"message": "post data"})
