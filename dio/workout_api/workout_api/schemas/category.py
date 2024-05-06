from typing import Annotated

from pydantic import UUID4, Field

from workout_api.contrib import BaseSchema


class CategorySchemaIn(BaseSchema):
    name: Annotated[
        str,
        Field(
            description="Category name",
            example="Scale",
            max_length=50,
        ),
    ]


class CategorySchemaOut(CategorySchemaIn):
    id: Annotated[UUID4, Field(description="ID")]
