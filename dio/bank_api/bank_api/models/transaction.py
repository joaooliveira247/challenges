import enum
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import Enum
from sqlalchemy.types import BIGINT

from bank_api.contrib.models import BaseModel
from bank_api.models.accounts import AccountModel


class TransactionStatusEnum(enum.StrEnum):
    NO_RESOURSES = "no_resourses"
    REFUND = "refund"
    ACCEPT = "accept"


class TransactionTypeEnum(enum.StrEnum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class TransactionModel(BaseModel):
    __tablename__: str = "transactions"

    amount: Mapped[BIGINT] = mapped_column(BIGINT, nullable=False)
    balance_after: Mapped[BIGINT] = mapped_column(BIGINT, nullable=False)
    status: Mapped[TransactionStatusEnum] = mapped_column(
        Enum(
            TransactionStatusEnum,
            name="transaciont_status_enum",
            native_enum=True,
        ),
        default=TransactionStatusEnum.ACCEPT,
        nullable=False,
    )

    account_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False
    )
    account: Mapped[AccountModel] = relationship(AccountModel, lazy="selectin")
