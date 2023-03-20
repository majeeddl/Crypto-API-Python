from flask import jsonify
from flask_restful import Resource

from use_cases.trade.trade_useCase import TradingUseCases


class TradingPositionsResource(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.tradingUseCases = TradingUseCases()

    def get(self):
        return jsonify(self.tradingUseCases.fetch_positions())
