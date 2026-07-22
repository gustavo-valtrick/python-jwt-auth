from src.models.interface.user_repository import UserRepositoryInterface


class UserRegister:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository
