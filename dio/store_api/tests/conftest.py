from asyncio import get_event_loop_policy
from pytest import fixture
from store_api.db import db_client
from store_api.schemas import ProductIn
from tests.factories import product_data
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient


@fixture(scope="session")
def event_loop():
    loop = get_event_loop_policy().new_event_loop()
    yield loop


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
def product_id():
    return UUID("b065336f-a3d5-42a1-a45a-9a01566e97be")


@fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)
