

from dependency_injector import containers, providers

# from use_cases.exchange.exchange_useCase import ExchangeUseCases
from use_cases.user.users_useCase import UserUseCases


class UseCasesContainer(containers.DeclarativeContainer):

    # config = providers.Configuration()

    userUseCase  = providers.Factory(
        UserUseCases,
        # config=config
    )

    # exchangeUseCase = providers.Container(
    #     ExchangeUseCases
    # )

    pass
