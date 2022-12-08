
from abc import abstractmethod
import pymongo
from typing import Generic, TypeVar

T = TypeVar('T')


class MongoRepository(Generic[T]):

    def __init__(self, collection_name) -> None:
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client['crypto-dev']
        self.collection = self.database[collection_name]

    @abstractmethod
    def find(self,options) -> list[T]:
        return self.collection.find()

    @abstractmethod
    def findById(self, id: str) -> T:
        return self.collection.find_one({'_id': id})

    @abstractmethod
    def create(self, entity: T) -> T:
        return self.collection.insert_one(entity)
