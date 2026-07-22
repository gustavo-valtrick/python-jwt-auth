import jwt
from datetime import datetime, timedelta, timezone


class JwtHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload={
                "exp": datetime.now(timezone.utc) + timedelta(minutes=1),
                **body,
            },
            key="65aYYS8GrCzsAlKCH6ierMhis7eZ3cmC",
            algorithm="HS256",
        )

        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(
            jwt=token,
            key="65aYYS8GrCzsAlKCH6ierMhis7eZ3cmC",
            algorithms="HS256",
        )

        return token_information
