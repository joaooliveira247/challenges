from datetime import datetime, timedelta, timezone
from typing import Any

from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError

from bank_api.contrib.errors import TokenError, UnexpectedError
from bank_api.core.config import get_settings
from bank_api.models.accounts import AccountModel

settings = get_settings()


def gen_jwt(account: AccountModel) -> str:
    payload: dict[str, Any] = {
        "sub": str(account.id),
        "exp": datetime.now(timezone.utc)
        + timedelta(minutes=settings.JWT_DEFAULT_LIFE_TIME),
        "iat": datetime.now(timezone.utc),
        "role": account.role,
    }

    return jwt.encode(payload, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)


def verify_token_jwt(token: str) -> dict[str, Any] | None:
    try:
        decoded = jwt.decode(
            token, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM
        )
        return decoded
    except (ExpiredSignatureError, JWTError) as e:
        raise TokenError(
            str(e),
            "core.token",
        )
    except Exception as e:
        raise UnexpectedError(str(e), "TokenError", "core.token")
