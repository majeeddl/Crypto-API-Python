

from domain.entities.base_entity import BaseEntity
from domain.enums.exchange_enums import ExchangeTypeEnum


class ExchangeConfig():
    def __init__(self, api_key, api_secret) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        pass


class Exchange(BaseEntity):

    name: str
    description: str
    type: ExchangeTypeEnum
    config: ExchangeConfig

    def __init__(self, name, config, type=ExchangeTypeEnum.bybit, description="") -> None:
        super().__init__()
        self.name = name
        self.description = description
        self.type = type
        self.config = config
