

from domain.entities.user_entity import User
from frameworks.data_services.mongo.repository.mongo_repository import MongoRepository



def mongo_repo_init():
    try:
        mongoRepository = MongoRepository[User]()
        result = mongoRepository.find()
        assert False
    except:
        assert True
    

def mongo_repo_init():
    try:
        mongoRepository = MongoRepository[User]()
        result = mongoRepository.find()
        assert False
    except:
        assert True
