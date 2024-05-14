from decimal import Decimal
from typing import Optional, Annotated
from bson import Decimal128

from pydantic import (
    BaseModel,
    Field,
    PositiveInt,
    AfterValidator,
)

from store_api.schemas.base import BaseSchemaMixin, OutMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: PositiveInt = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutMixin):
    ...


Decimal_ = Annotated[Decimal, AfterValidator(lambda v: Decimal128(str(v)))]


class ProductUpdate(ProductBase):
    quantity: Optional[PositiveInt] = Field(None, description="Product quantity")
    price: Optional[Decimal_] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductUpdate, OutMixin):
    ...
