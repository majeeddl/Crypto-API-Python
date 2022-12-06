import os
import websocket

from flask import Flask
from dependency_injector.wiring import Provide, inject

from adapters.api import initAPI
from configuration.config import ENV_PORT, ENV_DEBUG
from containers import Container
from use_cases.user.users_useCase import UserUseCases


# if __name__ == 'main':

# @inject
# def test(userUseCases: UserUseCases = Provide[Container.useCases.userUseCase]):
#     print(userUseCases.getUsers())


def create_app() -> Flask:

    container = Container()

    app = Flask(__name__)
    container.wire(modules=[".adapters"])
    # app.container = container

    initAPI(app)

    # test()

    # app.run(debug=ENV_DEBUG, port=ENV_PORT, use_reloader=False, threaded=True)

    return app
