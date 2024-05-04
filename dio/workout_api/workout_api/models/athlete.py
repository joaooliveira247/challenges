from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime, Float, Integer, String

from workout_api.contrib.models import BaseModel


class AthleteModel(BaseModel):
    __tablename__ = "Athletes"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=True)
    ssn: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float(2), nullable=False)
    height: Mapped[float] = mapped_column(Float(2), nullable=False)
    sex: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
