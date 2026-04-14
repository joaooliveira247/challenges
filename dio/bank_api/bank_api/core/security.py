from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from bank_api.core.config import get_settings

settings = get_settings()

pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_schema: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_PATH}/account/sign-in"
)
