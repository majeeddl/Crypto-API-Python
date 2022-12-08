from flask_restful import Api

from adapters.resources.home_resource import HomeResource
from use_cases.user.users_useCase import UserUseCases


def initAPI(app):

    api = Api(app)

    api.add_resource(HomeResource, "/")
