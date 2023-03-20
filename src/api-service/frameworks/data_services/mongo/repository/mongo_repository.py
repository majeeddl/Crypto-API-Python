from datetime import datetime
from abc import abstractmethod
from typing import Generic, TypeVar

from domain.utils.shared_utils import ConvertDictToClass, DictFromClass, DictToObj

import pymongo
from bson.objectid import ObjectId

T = TypeVar('T')


class MongoRepository(Generic[T]):

    def __init__(self, collection_name) -> None:
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client['crypto-dev']
        self.collection = self.database[collection_name]

    @abstractmethod
    def find(self) -> list[T]:
        return list(map(lambda x: DictToObj(x), self.collection.find()))

    @abstractmethod
    def findOne(self, query) -> T:
        findOne = self.collection.find_one(query)
        return DictToObj(findOne) if findOne else None

    @abstractmethod
    def findById(self, id: str) -> T:
        try:
            return DictToObj(self.findOne({'_id': id}))
        except Exception:
            return None

    @abstractmethod
    def create(self, entity: T) -> T:
        return self.collection.insert_one(entity.__dict__).inserted_id

    @abstractmethod
    def update(self, entity: T) -> T:
        if ObjectId.is_valid(entity._id):
            _id = ObjectId(entity._id)

        # _set = entity.__dict__
        _set = DictFromClass(entity)

        _set.pop('_id', None)

        return self.collection.update_one({"_id": _id}, {"$set": _set})

    @abstractmethod
    def deleteById(self, id: str) -> None:
        self.collection.delete_one({'_id': id})

    @abstractmethod
    def delete(self, query) -> None:
        self.collection.find_one_and_delete(query)
