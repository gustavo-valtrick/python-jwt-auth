from src.controllers.interfaces.user_register import UserRegisterInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class UserRegisterView(ViewInterface):
    def __init__(self, user_register: UserRegisterInterface):
        self.__controller = user_register

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body.get("username")
        password = http_request.body.get("password")
        self.__validate_inputs(username=username, password=password)

        response = self.__controller.registry(username=username, password=password)
        return HttpResponse(body={"data": response}, status_code=201)

    def __validate_inputs(self, username: any, password: any) -> None:
        if (
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ):
            raise Exception("Invalid Input")
