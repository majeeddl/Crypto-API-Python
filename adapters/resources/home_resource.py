from flask import jsonify
from flask_restful import Resource

from configuration.config import Config

class HomeResource(Resource):

    def get(self):
        return jsonify({"message": "hello world"})

    def post(self):
        return jsonify({"message": "post data"})

