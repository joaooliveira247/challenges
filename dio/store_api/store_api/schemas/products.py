from typing import Optional

from pydantic import BaseModel, Field, PositiveFloat, PositiveInt, UUID4

from store_api.schemas.base import BaseSchemaMixin

from datetime import datetime


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: PositiveInt = Field(..., description="Product quantity")
    price: PositiveFloat = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()


class ProductUpdate(ProductBase):
    quantity: Optional[PositiveInt] = Field(None, description="Product quantity")
    price: Optional[PositiveFloat] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductUpdate):
    ...
