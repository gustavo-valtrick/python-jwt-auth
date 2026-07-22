from .jwt_handler import JwtHandler


def test_jwt_handler():
    jwt_handler = JwtHandler()
    body = {
        "username": "HelloWorld",
        "email": "hello@world.com",
        "age": 21,
    }

    token = jwt_handler.create_jwt_token(body=body)
    token_informations = jwt_handler.decode_jwt_token(token=token)

    assert isinstance(token, str)

    assert "exp" in token_informations
    assert body.items() <= token_informations.items()
