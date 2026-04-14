from passlib.context import CryptContext

from bank_api.core.config import get_settings

settings = get_settings()

pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
