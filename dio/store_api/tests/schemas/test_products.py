from uuid import UUID


from store_api.schemas import ProductIn
from tests.factories import product_data


def test_schemas_return_success():
    data = product_data()
    product = ProductIn(**data)

    assert product.name == "Iphone 14 Pro Max"
    assert isinstance(product.id, UUID)
