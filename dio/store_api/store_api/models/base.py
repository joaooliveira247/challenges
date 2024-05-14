from datetime import datetime
from uuid import uuid4
from typing import Any
from decimal import Decimal
from bson import Decimal128

from pydantic import UUID4, BaseModel, Field, model_serializer


class CreateBaseModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @model_serializer
    def set_model(self) -> dict[str, Any]:
        model_dict = dict(self)

        for key, value in model_dict.items():
            if isinstance(value, Decimal):
                model_dict[key] = Decimal128(str(value))

        return model_dict
