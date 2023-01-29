from flask_restful import Api

from adapters.resources.home_resource import HomeResource
from adapters.resources.trading.trading_positions_resource import TradingPositionsResource


def initAPI(app):

    api = Api(app)

    api.add_resource(HomeResource, "/api/v1")

    api.add_resource(TradingPositionsResource,"/api/v1/trading/positions")
