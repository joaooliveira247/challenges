from store_api.core import settings
from motor.motor_asyncio import AsyncIOMotorClient
from asyncio import run


class MongoClient:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(
            settings.DATABASE_URL,
        )

    async def __test_connection(self) -> None:
        try:
            await self.client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def test_connection(self) -> None:
        run(self.__test_connection())

    def get_client(self) -> AsyncIOMotorClient:
        return self.client


db_client = MongoClient()
