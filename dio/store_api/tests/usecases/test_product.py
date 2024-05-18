from uuid import UUID

from pytest import raises, mark

from store_api.core.exceptions import DBNotFoundValueException, ProductAlreadyExists
from store_api.schemas import ProductOut, ProductUpdateOut
from store_api.usecases import product_usecase


async def test_usecases_create_should_return_sucess(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_create_double_raise_exception(product_in, product_inserted):
    with raises(ProductAlreadyExists) as err:
        await product_usecase.create(body=product_in)

    assert err.value.message == f"Product already exists in id: {product_inserted.id}"


async def test_usecases_get_should_return_success(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

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


@mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, list)
    assert len(result) > 1


async def test_usecases_update_should_return_success(product_inserted, product_up):
    product_up.price = "7500.00"
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_update_should_raise_not_found_exception(
    product_id,
    product_up,
):
    with raises(DBNotFoundValueException) as err:
        await product_usecase.update(product_id, product_up)

    assert err.value.message == f"Product not found at id {product_id}"


async def test_usecases_delete_return_success(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

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
