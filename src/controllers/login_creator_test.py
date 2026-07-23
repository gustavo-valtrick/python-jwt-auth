import pytest
from unittest.mock import create_autospec
from src.models.interface.user_repository import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler
from .login_creator import LoginCreator

_USER_ID = 123
_USERNAME = "myUsername"
_PASSWORD = "myP455Word!"
_WRONG_PASSWORD = "wrongPassword123"
_HASHED_PASSWORD = PasswordHandler().encrypt_password(password=_PASSWORD)
_VALID_USER_DB_RETURN = (_USER_ID, _USERNAME, _HASHED_PASSWORD)


def test_create():
    user_repository: UserRepositoryInterface = create_autospec(
        spec=UserRepositoryInterface,
        instance=True,
    )
    user_repository.get_user_by_username.return_value = _VALID_USER_DB_RETURN

    login_creator = LoginCreator(user_repository=user_repository)
    response = login_creator.create(
        username=_USERNAME,
        password=_PASSWORD,
    )

    user_repository.get_user_by_username.assert_called_once_with(username=_USERNAME)

    assert response["access"] == True
    assert response["username"] == _USERNAME
    assert isinstance(response["token"], str)
    assert response["token"].count(".") == 2
    assert response["token"].startswith("eyJ")


def test_create_with_wrong_password():
    user_repository: UserRepositoryInterface = create_autospec(
        spec=UserRepositoryInterface,
        instance=True,
    )
    user_repository.get_user_by_username.return_value = _VALID_USER_DB_RETURN

    login_creator = LoginCreator(user_repository=user_repository)

    with pytest.raises(expected_exception=Exception) as excinfo:
        login_creator.create(
            username=_USERNAME,
            password=_WRONG_PASSWORD,
        )

    user_repository.get_user_by_username.assert_called_once_with(username=_USERNAME)

    assert str(excinfo.value) == "Wrong Password"
