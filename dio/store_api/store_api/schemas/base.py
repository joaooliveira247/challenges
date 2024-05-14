from pydantic import BaseModel, ConfigDict, UUID4, Field, model_validator
from datetime import datetime
from bson import Decimal128
from decimal import Decimal


class BaseSchemaMixin(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class OutMixin(BaseModel):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    @model_validator(mode="before")
    def set_schema(cls, data: dict):
        for key, value in data.items():
            if isinstance(value, Decimal128):
                data[key] = Decimal(str(value))

        return data
