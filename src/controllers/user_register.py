from src.models.interface.user_repository import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler


class UserRegister:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository
        self.__password_handler = PasswordHandler()

    def registry(self, username: str, password: str) -> dict:
        hashed_password = self.__create_hash_password(password=password)
        self.__registry_new_user(username=username, hashed_password=hashed_password)
        return self.__format_response(username=username)

    def __create_hash_password(self, password: str) -> str:
        hashed_password = self.__password_handler.encrypt_password(password=password)
        return hashed_password

    def __registry_new_user(self, username: str, hashed_password: str) -> None:
        self.__user_repository.registry_user(
            username=username, password=hashed_password
        )

    def __format_response(self, username: str) -> dict:
        return {
            "type": "User",
            "count": 1,
            "username": username,
        }
