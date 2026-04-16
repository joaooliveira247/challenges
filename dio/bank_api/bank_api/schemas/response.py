from uuid import UUID

from pydantic import BaseModel


class CreatedSchameMixin(BaseModel):
    id: UUID


class AccountCreatedSchema(CreatedSchameMixin): ...
