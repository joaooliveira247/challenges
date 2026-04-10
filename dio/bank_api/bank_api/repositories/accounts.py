from uuid import UUID

from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.ext.asyncio import AsyncSession

from bank_api.contrib.errors import DatabaseError, UnexpectedError
from bank_api.contrib.repositories import BaseRepository
from bank_api.models.accounts import AccountModel


class AccountsRepository(BaseRepository):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(db)

    async def create(self, account: AccountModel) -> UUID | None:
        try:
            self.db.add(account)
            await self.db.flush()
            await self.db.commit()
            return account.id
        except (OperationalError, IntegrityError) as e:
            await self.db.rollback()
            raise DatabaseError(str(e), self.__class__.__name__)
        except Exception as e:
            await self.db.rollback()
            raise UnexpectedError(
                str(e), location="database", resource=self.__class__.__name__
            )
