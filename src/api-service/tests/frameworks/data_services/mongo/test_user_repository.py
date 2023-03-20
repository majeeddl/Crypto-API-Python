
from domain.entities.user_entity import User
from frameworks.data_services.mongo.repository.user_repository import UserRepository
import pytest


@pytest.fixture()
def clean_up():
    userRepository = UserRepository()
    userRepository.delete({'username': 'test_user'})
    userRepository.delete({'username': 'test_findOne_user'})
    userRepository.delete({'username': 'test_update_user'})


def test_repository_findOneUser(clean_up):

    userRepository = UserRepository()

    newUser = User("test_findOne_user", "test_findOne_user", password=1234)

    userRepository.create(newUser)

    findUser: User = userRepository.findOne({"name": "test_findOne_user"})

    assert findUser.name == 'test_findOne_user'


def test_repository_createUser(clean_up):

    userRepository = UserRepository()

    newUser = User("test_user", "test_user", password=1234)

    createduserId = userRepository.create(newUser)

    assert createduserId != None


def test_respository_updateUser():

    userRepository = UserRepository()

    newUser = User("test_update_user", "test_update_user", password=1234)

    userRepository.create(newUser)

    findUser: User = userRepository.findOne({'username': 'test_update_user'})

    findUser.name = "test_user_name_updated"

    result = userRepository.update(findUser)

    assert result != None


def test_respository_deleteUser():

    userRepository = UserRepository()

    newUser = User("delete_user", "delete_user", password=1234)

    createdUserId = userRepository.create(newUser)

    result = userRepository.deleteById(createdUserId)

    findDeletedUser: User = userRepository.findById(createdUserId)

    assert findDeletedUser == None
