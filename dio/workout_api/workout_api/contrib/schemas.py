from pydantic import BaseModel
from pydantic import UUID4
from datetime import datetime
from typing import Annotated
from pydantic import Field


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_atributes = True


class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description="ID")]
    created_at: Annotated[datetime, Field(description="Creation Date")]
