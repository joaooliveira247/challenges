from decimal import Decimal
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field


class CreatedSchameMixin(BaseModel):
    id: UUID


class AccountCreatedSchema(CreatedSchameMixin): ...


class AccountTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


Money = Annotated[Decimal, Field(gt=0)]
