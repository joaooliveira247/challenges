from pydantic import BaseModel, UUID4, Field
from uuid import uuid4
from datetime import datetime


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
