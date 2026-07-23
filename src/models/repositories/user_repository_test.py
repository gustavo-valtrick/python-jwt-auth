from unittest.mock import Mock
from src.models.settings.db_connection_handler import db_connection_handler
from .user_repository import UserRepository


class MockCursor:
    def __init__(self):
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection:
    def __init__(self):
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_registry_user() -> None:
    username = "Freddy"
    password = "Yabadabado"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.registry_user(username=username, password=password)

    cursor = mock_connection.cursor.return_value

    assert isinstance(cursor, MockCursor)

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)

    mock_connection.commit.assert_called_once()


def test_edit_balance() -> None:
    user_id = 234
    balance = 100.11

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.edit_balance(user_id=user_id, new_balance=balance)

    cursor = mock_connection.cursor.return_value

    assert isinstance(cursor, MockCursor)

    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (balance, user_id)

    mock_connection.commit.assert_called_once()


def test_get_user_by_username():
    username = "meuUserName"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.get_user_by_username(username=username)

    cursor = mock_connection.cursor.return_value

    assert isinstance(cursor, MockCursor)

    assert "SELECT id, username, password, balance" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)

    cursor.fetchone.assert_called_once()
