


from domain.entities.user_entity import User
from frameworks.data_services.mongo.repository.mongo_repository import MongoRepository
import pytest


collection_name='test_mongo'


@pytest.fixture()
def clean_up():
    userRepository = MongoRepository[User](collection_name)
    userRepository.delete({'username': 'test'})


def test_check_error_forLackingCollectionName():
    try:
        mongoRepository = MongoRepository[User]()
        result = mongoRepository.find()
        assert False
    except Exception as e:
        assert True


def test_mongo_init():
    try:
        mongoRepository = MongoRepository[User](collection_name)
        assert True
    except Exception as e:
        assert False


def test_mongo_find():
    try:
        mongoRepository = MongoRepository[User](collection_name)
        result = mongoRepository.find()
        print(result)
        assert True
    except Exception as e:
        assert False


def test_mongo_create(clean_up):
    try:
        mongoRepository = MongoRepository[User](collection_name)
        createdId = mongoRepository.create(User('test','test'))
        assert createdId != None
    except Exception as e:
        assert False


def test_mongo_update():
    try:
        mongoRepository = MongoRepository[User](collection_name)
        findOne = mongoRepository.findOne({ "username" : 'test'})
        findOne.name = 'name_update'
        mongoRepository.update(findOne)
        findUpdated = mongoRepository.findOne({"username": 'test'})
        assert findUpdated.name == 'name_update'
    except Exception as e:
        assert False


def test_mongo_delete():
    try:
        mongoRepository = MongoRepository[User](collection_name)
        mongoRepository.delete({'username': 'test'})
        findDeleted= mongoRepository.findOne({"username": 'test'})
        assert findDeleted == None
    except Exception as e:
        assert False


