from uuid import UUID, uuid4

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import TIMESTAMP


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        default=uuid4,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
