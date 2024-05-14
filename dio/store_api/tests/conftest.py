from asyncio import get_event_loop_policy
from typing import AsyncGenerator
from uuid import UUID

from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from pytest import fixture

from store_api import app
from store_api.db import db_client
from store_api.schemas import ProductIn, ProductUpdate
from store_api.usecases import product_usecase
from tests.factories import product_data, products_data


@fixture(scope="session")
def event_loop():
    loop = get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@fixture
def mongo_client() -> AsyncIOMotorClient:
    return db_client.get_client()


@fixture(autouse=True)
async def clear_collections(mongo_client: AsyncIOMotorClient):
    yield
    collections_names = await mongo_client.get_database().list_collection_names()
    for collection_name in collections_names:
        if collection_name.startswith("system"):
            continue

        await mongo_client.get_database()[collection_name].delete_many({})


@fixture
async def client() -> AsyncGenerator[AsyncClient]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@fixture
async def products_url() -> str:
    return "/products/"


@fixture
def product_id():
    return UUID("b065336f-a3d5-42a1-a45a-9a01566e97be")


@fixture
def product_in(product_id):
    product = ProductIn(**product_data(), id=product_id)

    return product


@fixture
def products_in():
    return [ProductIn(**product) for product in products_data()]


@fixture
def product_up(product_id):
    return ProductUpdate(**product_data(), id=product_id)


@fixture
async def product_inserted(product_in):
    return await product_usecase.create(body=product_in)


@fixture
async def products_inserted(products_in):
    return [await product_usecase.create(body=product) for product in products_in]
