
from src.shared.entities.base_entity import BaseEntity
from src.shared.enums.exchange_type_enum import ExchangeTypeEnum

class Exchange(BaseEntity):
    type: ExchangeTypeEnum
    name: str
    description: str

    def __init__(self, type, name, description) -> None:
        super().__init__()
        self.type = type
        self.name = name
        self.description = description
        if not hasattr(self, '_id'):
            self.createdAt = datetime.now()
