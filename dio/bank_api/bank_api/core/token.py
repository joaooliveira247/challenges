from datetime import datetime, timedelta, timezone
from typing import Any
from bank_api.core.config import get_settings
from bank_api.models.accounts import AccountModel
from jose import jwt


settings = get_settings()

def gen_jwt(life_time: float, account: AccountModel) -> str:
    payload: dict[str, Any] = {
        "sub": str(account.id),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=life_time),
        "iat": datetime.now(timezone.utc),
        "role": account.role
    }
    
    return jwt.encode(payload, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)