import os
import websocket

from flask import Flask, jsonify, Request
# from dependency_injector.wiring import Provide, inject


from adapters.api import initAPI
from configuration.config import ENV_PORT, ENV_DEBUG
from containers import Container
# from containers import Containers
# from use_cases.user.users_useCase import UserUseCases

# containers = Containers()
# containers.wire(modules=[__name__])

container = Container()

app = Flask(__name__)
# app.container = containers
app.container = container

initAPI(app)

app.run(debug=ENV_DEBUG, port=ENV_PORT, use_reloader=False, threaded=True)



# if __name__ == 'main':
    
