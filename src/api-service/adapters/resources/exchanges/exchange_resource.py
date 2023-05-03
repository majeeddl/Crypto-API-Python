from flask import jsonify
from flask_restful import Resource, request, reqparse, marshal_with
from domain.entities.exchange_entity import Exchange
from use_cases.exchange.exchange_useCase import ExchangeUseCases
import json


class ExchangesResource(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.exchangeUseCases = ExchangeUseCases()

    def get(self):
        exchanges = self.exchangeUseCases.getExchanges()
        # print(jsonify(exchanges))

        return exchanges

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        exchange = Exchange(
            **json_data
        )

        self.exchangeUseCases.createExchange(exchange)
        return {"message": "Hello, World!"}

    def put(self):
        json_data = request.get_json(force=True)
        return jsonify(self.exchangeUseCases.update_exchange(request.json))
