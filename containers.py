

from dependency_injector import containers, providers

from use_cases.useCases_container import UseCasesContainer


class Container(containers.DeclarativeContainer):

    useCases = providers.Container(
        UseCasesContainer
    )
