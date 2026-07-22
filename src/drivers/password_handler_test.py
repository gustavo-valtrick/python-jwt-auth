from .password_handler import PasswordHandler


def test_encrypt():
    my_password = "MyPassword@123"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(password=my_password)

    assert hashed_password

    assert password_handler.check_password(
        password=my_password,
        hashed_password=hashed_password,
    )
