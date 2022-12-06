
import pymongo
from typing import Generic, TypeVar

T = TypeVar('T')


class MongoRepository(Generic[T]):

    def __init__(self) -> None:
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client['crypto-dev']
        self.collection = self.database[T]

    def find(self) -> list[T]:
        return self.collection.find()

    def findById(self, id: str) -> T:
        return self.collection.find_one({'_id': id})
