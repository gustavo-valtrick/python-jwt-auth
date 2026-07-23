from unittest.mock import create_autospec
from src.models.interface.user_repository import UserRepositoryInterface
from .balance_editor import BalanceEditor

_USER_ID = 123
_NEW_BALANCE = 786.46


def test_edit() -> None:
    user_repository: UserRepositoryInterface = create_autospec(
        spec=UserRepositoryInterface, instance=True
    )

    balance_editor = BalanceEditor(user_repository=user_repository)
    response = balance_editor.edit(
        user_id=_USER_ID,
        new_balance=_NEW_BALANCE,
    )

    user_repository.edit_balance.assert_called_once_with(
        user_id=_USER_ID,
        new_balance=_NEW_BALANCE,
    )

    assert response == {
        "type": "User",
        "count": 1,
        "new balance": _NEW_BALANCE,
    }
