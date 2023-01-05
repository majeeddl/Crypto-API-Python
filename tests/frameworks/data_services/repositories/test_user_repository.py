
from domain.entities.user_entity import User
from frameworks.data_services.mongo.repository.user_repository import UserRepository
import pytest


@pytest.fixture()
def clean_up():
    userRepository = UserRepository()
    userRepository.delete({'username': 'test_user'})


def test_createUserTest(clean_up):

    userRepository = UserRepository()

    newUser = User("test_user", "test_user", password=1234)

    createduserId = userRepository.create(newUser)

    assert createduserId != None


def test_2():
    print('two')
