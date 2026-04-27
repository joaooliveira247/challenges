from uuid import UUID

from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from bank_api.contrib.errors import DatabaseError, UnexpectedError
from bank_api.contrib.repositories import BaseRepository
from bank_api.models.transaction import TransactionModel


class TransactionsRepository(BaseRepository):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(db)

    async def create(self, transaction: TransactionModel) -> UUID:
        try:
            self.db.add(transaction)
            await self.db.flush()
            await self.db.commit()
            return transaction.id
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

    async def get_all_account_transactions(
        self, account_id: UUID
    ) -> list[TransactionModel]:
        async with self.db as session:
            try:
                result = await session.execute(
                    select(TransactionModel)
                    .filter(TransactionModel.account_id == account_id)
                    .options(joinedload(TransactionModel.account))
                )

                transactions: list[TransactionModel] = list(
                    result.scalars().all()
                )
                return transactions
            except OperationalError as e:
                raise DatabaseError(str(e), self.__class__.__name__)
            except Exception as e:
                raise UnexpectedError(
                    str(e),
                    location="database",
                    resource=self.__class__.__name__,
                )
