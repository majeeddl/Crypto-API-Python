from flask import jsonify
from flask_restful import Resource


class HomeApi(Resource):

    def get(self):
        return jsonify({"message": "hello world"})

    def post(self):
        return jsonify({"message": "post data"})

