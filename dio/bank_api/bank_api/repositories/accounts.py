from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.ext.asyncio import AsyncSession

from bank_api.contrib.errors import DatabaseError, UnexpectedError
from bank_api.contrib.repositories import BaseRepository
from bank_api.models.accounts import AccountModel, AccountStatusEnum


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
        finally:
            await self.db.close()

    async def get_account_by_id(self, id: UUID) -> AccountModel | None:
        async with self.db as session:
            try:
                result = await session.execute(
                    select(AccountModel).filter(AccountModel.id == id)
                )

                account = result.scalars().one_or_none()
                return account
            except OperationalError as e:
                await self.db.rollback()
                raise DatabaseError(str(e), self.__class__.__name__)
            except Exception as e:
                await self.db.rollback()
                raise UnexpectedError(
                    str(e),
                    location="database",
                    resource=self.__class__.__name__,
                )

    async def get_account_by_query(
        self, email: str | None, ssn: str | None
    ) -> AccountModel | None:
        async with self.db as session:
            statment = select(AccountModel)

            if email:
                statment = statment.filter(AccountModel.email == email)
            if ssn:
                statment = statment.filter(AccountModel.ssn == ssn)

            try:
                result = await session.execute(statment)
                account = result.scalars().one_or_none()
                return account
            except OperationalError as e:
                await self.db.rollback()
                raise DatabaseError(str(e), self.__class__.__name__)
            except Exception as e:
                await self.db.rollback()
                raise UnexpectedError(
                    str(e),
                    location="database",
                    resource=self.__class__.__name__,
                )

    async def update_account(self, account_id: UUID, fields: dict) -> None:
        async with self.db as session:
            try:
                result = await session.execute(
                    select(AccountModel).filter(AccountModel.id == account_id)
                )

                if update_account := result.scalars().one_or_none():
                    for k, v in fields:
                        setattr(update_account, k, v)

                    await session.flush()
                    await session.commit()
                    return
            except (OperationalError, IntegrityError) as e:
                await self.db.rollback()
                raise DatabaseError(str(e), resource=self.__class__.__name__)
            except Exception as e:
                await self.db.rollback()
                raise UnexpectedError(
                    str(e),
                    location="database",
                    resource=self.__class__.__name__,
                )

    async def delete_account(self, account_id: UUID) -> None:
        async with self.db as session:
            try:
                result = await session.execute(
                    select(AccountModel).filter(AccountModel.id == account_id)
                )

                if delete_account := result.scalars().one_or_none():
                    delete_account.status = AccountStatusEnum.DEACTIVATED

                    await session.flush()
                    await session.commit()
                    return
            except (OperationalError, IntegrityError) as e:
                await self.db.rollback()
                raise DatabaseError(str(e), resource=self.__class__.__name__)
            except Exception as e:
                await self.db.rollback()
                raise UnexpectedError(
                    str(e),
                    location="database",
                    resource=self.__class__.__name__,
                )
