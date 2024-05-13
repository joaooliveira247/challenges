from pydantic import Field, PositiveFloat, PositiveInt

from store_api.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):
    name: str = Field(..., description="Product name")
    quantity: PositiveInt = Field(..., description="Product quantity")
    price: PositiveFloat = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductOut(ProductIn):
    ...
