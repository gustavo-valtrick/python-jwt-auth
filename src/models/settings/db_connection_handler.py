import sqlite3
from sqlite3 import Connection


class _DbConnectionHandler:
    def __init__(self):
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> None:
        self.__conn = sqlite3.connect(
            database=self.__connection_string,
            check_same_thread=False,
        )

    def get_connection(self) -> Connection:
        return self.__conn


db_connection_handler = _DbConnectionHandler()
