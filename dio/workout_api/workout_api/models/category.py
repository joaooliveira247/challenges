from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Integer, String

from workout_api.contrib import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = "category"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=True, unique=True)
    athlete: Mapped["AthleteModel"] = relationship(back_populates="category")
