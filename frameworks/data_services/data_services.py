

from domain.abstracts.data_service_abstract import DataServicesAbstract
from frameworks.data_services.mongo.mongo_data_services import MongoDataServices


class DataServices(MongoDataServices):

    def __init__(self) -> None:
        super().__init__()
