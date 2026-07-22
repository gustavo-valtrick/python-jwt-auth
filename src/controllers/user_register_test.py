from unittest.mock import create_autospec
from src.models.interface.user_repository import UserRepositoryInterface
from .user_register import UserRegister


def test_registry():
    repository: UserRepositoryInterface = create_autospec(spec=UserRepositoryInterface)
    controller = UserRegister(user_repository=repository)

    username = "HelloWorld"
    password = "H3lloW0rld!"

    response = controller.registry(username=username, password=password)

    assert response["type"] == "User"
    assert response["username"] == username

    registry_user_attributes = repository.registry_user.call_args.kwargs

    assert registry_user_attributes["username"] == username
    assert registry_user_attributes["password"] is not None
    assert registry_user_attributes["password"] != password
