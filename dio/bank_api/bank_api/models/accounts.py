import enum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Enum
from sqlalchemy.types import BIGINT, CHAR, VARCHAR

from bank_api.contrib.models import BaseModel


class AccountStatusEnum(enum.StrEnum):
    ACTIVATED = "activated"
    DEACTIVATED = "deactivated"
    BLOCKED = "blocked"


class AccountRoleEnum(enum.StrEnum):
    CUSTOMER = "customer"
    ADMIN = "admin"


class AccountModel(BaseModel):
    __tablename__: str = "accounts"

    full_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    email: Mapped[str] = mapped_column(
        VARCHAR(255), unique=True, nullable=False
    )
    ssn: Mapped[CHAR] = mapped_column(CHAR(11), unique=True, nullable=False)
    balance: Mapped[BIGINT] = mapped_column(BIGINT, default=0)
    status: Mapped[AccountStatusEnum] = mapped_column(
        Enum(AccountStatusEnum, name="status_enum", native_enum=True),
        default=AccountStatusEnum.ACTIVATED,
        nullable=False,
    )
    password: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    role: Mapped[AccountRoleEnum] = mapped_column(
        Enum(AccountRoleEnum, name="role_enum", native_enum=True),
        default=AccountRoleEnum.CUSTOMER,
        nullable=False,
    )
