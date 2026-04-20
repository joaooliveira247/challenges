from uuid import UUID

from pydantic import BaseModel


class CreatedSchameMixin(BaseModel):
    id: UUID


class AccountCreatedSchema(CreatedSchameMixin): ...


class AccountTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
