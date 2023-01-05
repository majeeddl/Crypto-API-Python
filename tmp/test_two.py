

from domain.entities.user_entity import User
from frameworks.data_services.mongo.repository.mongo_repository import MongoRepository


def test_two():
    assert True

# def test_mongo_init_needCollectionName():
#     try:
#         mongoRepository = MongoRepository[User]()
#         result = mongoRepository.find()
#         assert False
#     except Exception as e:
#         assert True

    # def test_mongo_init_finddata():
    #     try:
    #         mongoRepository = MongoRepository[User]('users')
    #         result = mongoRepository.find()
    #         print(result)
    #         assert True
    #     except Exception as e:
    #         assert False
