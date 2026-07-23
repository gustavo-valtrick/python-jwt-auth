from src.models.interface.user_repository import UserRepositoryInterface


class BalanceEditor:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_respository = user_repository

    def edit(self, user_id: int, new_balance: float) -> dict:
        self.__edit_balance(user_id=user_id, new_balance=new_balance)

        return self.__format_response(new_balance=new_balance)

    def __edit_balance(self, user_id: int, new_balance: float) -> None:
        self.__user_respository.edit_balance(user_id=user_id, new_balance=new_balance)

    def __format_response(self, new_balance: float) -> dict:
        return {
            "type": "User",
            "count": 1,
            "new balance": new_balance,
        }
