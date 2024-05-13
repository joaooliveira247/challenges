from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from store_api.db import db_client
from store_api.schemas import ProductIn


class ProductUseCase:
    def __init__(self) -> None:
        self.cliente: AsyncIOMotorClient = db_client.get_client()
        self.database: AsyncIOMotorDatabase = self.cliente.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> None:
        await self.collection.insert_one(body.model_dump())


product_usecase = ProductUseCase()
