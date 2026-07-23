import pytest
from unittest.mock import create_autospec
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.user_register import UserRegisterInterface
from .user_register_view import UserRegisterView

_USERNAME = "MyUsername"
_PASSWORD = "MyPassword"


def test_handle_user_register():
    body = {
        "username": _USERNAME,
        "password": _PASSWORD,
    }
    request = HttpRequest(body=body)

    mock_controller: UserRegisterInterface = create_autospec(
        spec=UserRegisterInterface, instance=True
    )
    mock_controller.registry.return_value = {
        "type": "User",
        "count": 1,
        "username": _USERNAME,
    }

    user_register_view = UserRegisterView(user_register=mock_controller)

    response = user_register_view.handle(http_request=request)

    mock_controller.registry.assert_called_once_with(
        username=_USERNAME, password=_PASSWORD
    )

    assert isinstance(response, HttpResponse)
    assert response.body["data"] == mock_controller.registry.return_value
    assert response.status_code == 201


def test_handle_user_register():
    body = {
        "password": _PASSWORD,
    }
    request = HttpRequest(body=body)

    mock_controller: UserRegisterInterface = create_autospec(
        spec=UserRegisterInterface, instance=True
    )
    mock_controller.registry.return_value = {
        "type": "User",
        "count": 1,
        "username": _USERNAME,
    }

    user_register_view = UserRegisterView(user_register=mock_controller)

    with pytest.raises(Exception) as excinfo:
        user_register_view.handle(http_request=request)

    mock_controller.registry.assert_not_called()

    assert str(excinfo.value) == "Invalid Input"
