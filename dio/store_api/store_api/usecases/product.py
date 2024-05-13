from uuid import UUID

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from store_api.core.exceptions import DBNotFoundValueException
from store_api.db import db_client
from store_api.schemas import ProductIn, ProductOut


class ProductUseCase:
    def __init__(self) -> None:
        self.cliente: AsyncIOMotorClient = db_client.get_client()
        self.database: AsyncIOMotorDatabase = self.cliente.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product = ProductOut(**body.model_dump())
        await self.collection.insert_one(product.model_dump())
        return product

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise DBNotFoundValueException(
                f"Product not found with UUID({id})",
            )
        return ProductOut(**result)


product_usecase = ProductUseCase()
