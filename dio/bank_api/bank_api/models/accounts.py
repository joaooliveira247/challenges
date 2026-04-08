from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import BIGINT, CHAR, VARCHAR

from bank_api.contrib.models import BaseModel


class AccountModel(BaseModel):
    __table_name__: str = "accounts"

    full_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    email: Mapped[str] = mapped_column(
        VARCHAR(255), unique=True, nullable=False
    )
    ssn: Mapped[CHAR] = mapped_column(CHAR(11), unique=True, nullable=False)
    balance: Mapped[BIGINT] = mapped_column(BIGINT, default=0)
