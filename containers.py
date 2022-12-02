from dependency_injector import containers, providers

# from use_cases.useCases_container import UseCasesContainer


# class Containers(containers.DeclarativeContainer):

#     useCases = providers.Container(
#         UseCasesContainer
#     )


from services import SearchService


class Container(containers.DeclarativeContainer):

    search_service = providers.Factory(
        SearchService
    )
