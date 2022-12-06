from flask_restful import Api
from dependency_injector.wiring import Provide, inject

from adapters.resources.home_resource import HomeResource
from containers import Container
from use_cases.user.users_useCase import UserUseCases


@inject
def initAPI(app, userUseCases: UserUseCases = Provide[Container.useCases.userUseCase]):

    print(userUseCases.getUsers())

    api = Api(app)

    api.add_resource(HomeResource, "/")
