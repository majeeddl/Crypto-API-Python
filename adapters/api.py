from flask_restful import Api

from adapters.resources.home_resource import HomeResource

def initAPI(app):

    api = Api(app)

    api.add_resource(HomeResource, "/")
