from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash

from bank_api.contrib.errors import PasswordHashError
from bank_api.core.config import get_settings

settings = get_settings()

pwd_context: PasswordHash = PasswordHash.recommended()

oauth2_schema: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_PATH}/account/sign-in"
)


def gen_hash(passwd: str) -> str:
    if not isinstance(passwd, str):
        raise ValueError("password must be a string")
        return
    return pwd_context.hash(passwd)


def check_password(passwd: str, hash_passwd: str) -> bool:
    try:
        return pwd_context.verify(passwd, hash_passwd)
    except Exception as e:
        raise PasswordHashError(resource="security", message=str(e))
