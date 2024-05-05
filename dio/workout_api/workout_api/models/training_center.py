from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Integer, String

from workout_api.contrib.models import BaseModel


class TrainingCenterModel(BaseModel):
    __tablename__ = "training_center"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=True)
    address: Mapped[str] = mapped_column(String(60), nullable=True)
    owner: Mapped[str] = mapped_column(String(30), nullable=True)
    athlete: Mapped["AthleteModel"] = relationship(
        back_populates="training_center",
    )
