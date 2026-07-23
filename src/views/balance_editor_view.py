from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class BalanceEditorView(ViewInterface):
    def __init__(self, controller: BalanceEditorInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.params.get("user_id")
        new_balance = http_request.body.get("new_balance")
        self.__validate_inputs(user_id=user_id, new_balance=new_balance)

        response = self.__controller.edit(user_id=user_id, new_balance=new_balance)
        return HttpResponse(body={"data": response}, status_code=200)

    def __validate_inputs(self, user_id: any, new_balance: any) -> None:
        if not user_id or not new_balance or not isinstance(new_balance, float):
            raise Exception("Invalid Input")
