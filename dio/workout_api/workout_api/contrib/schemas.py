from pydantic import BaseModel, UUID4, Field
from datetime import datetime
from typing import Annotated


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_atributes = True


class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description="ID")]
    created_at: Annotated[
        datetime, Field(description="Creation Date", default=datetime.now())
    ]
