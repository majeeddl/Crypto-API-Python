
from datetime import datetime
from domain.entities.base_entity import BaseEntity


class User(BaseEntity):
    username: str
    password: str
    name: str

    def __init__(self, username, name, password=None) -> None:
        super().__init__()
        self.username = username
        self.name = name
        self.password = password
        if not hasattr(self, '_id'):
            self.createdAt = datetime.now()
