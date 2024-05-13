from store_api.usecases import product_usecase
from store_api.schemas import ProductOut


async def test_usecases_create_should_return_sucess(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_sucess(product_in, product_id):
    # here i create a product 'cause fixture clear_collections delete all data
    await product_usecase.create(body=product_in)
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"
