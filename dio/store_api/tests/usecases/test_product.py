from uuid import UUID

from pytest import raises

from store_api.core.exceptions import DBNotFoundValueException
from store_api.schemas import ProductOut, ProductUpdateOut
from store_api.usecases import product_usecase


async def test_usecases_create_should_return_sucess(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_success(product_inserted, product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_not_found():
    with raises(DBNotFoundValueException) as err:
        await product_usecase.get(
            id=UUID("9b6efc62-acda-44fb-9f5f-9f86aa3efbd3"),
        )

    assert (
        err.value.message
        == "Product not found with UUID(9b6efc62-acda-44fb-9f5f-9f86aa3efbd3)"
    )


async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, list)


async def test_usecases_update_should_return_success(
    product_id, product_inserted, product_up
):
    product_up.price = 7500.00
    result = await product_usecase.update(id=product_id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_delete_return_success(product_id, product_inserted):
    result = await product_usecase.delete(id=product_id)

    assert result is True


async def test_usecases_delete_should_return_not_found():
    with raises(DBNotFoundValueException) as err:
        await product_usecase.get(
            id=UUID("9b6efc62-acda-44fb-9f5f-9f86aa3efbd3"),
        )

    assert (
        err.value.message
        == "Product not found with UUID(9b6efc62-acda-44fb-9f5f-9f86aa3efbd3)"
    )
