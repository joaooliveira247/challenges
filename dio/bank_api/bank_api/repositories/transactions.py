from sqlalchemy.ext.asyncio import AsyncSession

from bank_api.contrib.repositories import BaseRepository


class TransactionsRepository(BaseRepository):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(db)
