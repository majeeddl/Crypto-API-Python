

from domain.entities.base_entity import BaseEntity


class User(BaseEntity):

    username:str
    password:str
    name:str