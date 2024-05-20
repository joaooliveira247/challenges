from __future__ import annotations

from datetime import datetime
from uuid import UUID

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo import ReturnDocument
from pymongo.errors import OperationFailure

from store_api.core.exceptions import (
    DBNotFoundValueException,
    ProductAlreadyExists,
    FilterFailureException,
)
from store_api.db import db_client
from store_api.models import ProductModel
from store_api.schemas import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut


class ProductUseCase:
    def __init__(self) -> None:
        self.cliente: AsyncIOMotorClient = db_client.get_client()
        self.database: AsyncIOMotorDatabase = self.cliente.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product = ProductModel(**body.model_dump())
        exists = await self.collection.find_one({"name": body.name})
        if exists:
            raise ProductAlreadyExists(
                f"Product already exists in id: {exists['id']}",
            )
        await self.collection.insert_one(product.model_dump())
        return ProductOut(**product.model_dump())

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise DBNotFoundValueException(
                f"Product not found with UUID({id})",
            )
        return ProductOut(**result)

    async def query(self) -> list[ProductOut]:
        return [ProductOut(**product) async for product in self.collection.find()]

    async def query_filter(self, _filter: dict) -> list[ProductOut]:
        try:
            return [
                ProductOut(**product) async for product in self.collection.find(_filter)
            ]
        except OperationFailure:
            raise FilterFailureException(f"{_filter} not found any pattern.")

    async def update(self, id: UUID, body: ProductUpdate) -> ProductOut:
        product_up = body.model_dump(exclude_none=True)
        product_up["updated_at"] = datetime.now().strftime(
            "%Y-%m-%dT%H:%M:%S.%f",
        )
        result = await self.collection.find_one_and_update(
            {"id": id},
            update={"$set": product_up},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            raise DBNotFoundValueException(f"Product not found at id: {id}")
        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise DBNotFoundValueException(
                f"Product not found with UUID({id})",
            )

        result = await self.collection.delete_one({"id": id})
        return True if result.deleted_count > 0 else False


product_usecase = ProductUseCase()
