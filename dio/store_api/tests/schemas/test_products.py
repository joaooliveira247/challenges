from pydantic import ValidationError
from pytest import raises

from store_api.schemas import ProductIn
from tests.factories import product_data


def test_schemas_return_success(product_id):
    data = product_data()
    product = ProductIn(**data, id=product_id)

    assert product.name == "Iphone 14 Pro Max"


def test_schemas_raise_validation_error(product_id):
    data = product_data()
    data.pop("status")
    with raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 14 Pro Max", "quantity": 10, "price": 8500.0},
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }
