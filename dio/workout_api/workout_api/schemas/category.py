from workout_api.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import Field


class CategorySchema(BaseSchema):
    name: Annotated[
        str,
        Field(
            description="Category name",
            examples="Scale",
            max_length=50,
        ),
    ]
