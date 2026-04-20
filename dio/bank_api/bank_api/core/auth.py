from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from bank_api.contrib.errors import InvalidResource
from bank_api.core.security import check_password
from bank_api.models.accounts import AccountModel
from bank_api.repositories.accounts import AccountsRepository


async def authenticate(
    db: AsyncSession, email: EmailStr, passwd: str
) -> AccountModel:
    account_repository = AccountsRepository(db)

    account = await account_repository.get_account_by_query(email=email)

    if not account:
        raise InvalidResource(message="email")

    if not check_password(passwd, account.password):
        raise InvalidResource(message="password")

    return account
