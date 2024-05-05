from workout_api.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import Field


class TrainingCenterSchema(BaseSchema):
    name: Annotated[
        str,
        Field(
            description="Training center name",
            example="Tunder Bird",
            max_length=20,
        ),
    ]
    address: Annotated[
        str,
        Field(
            description="Training center address",
            example="495 Grove Street, New York - USA",
            max_length=20,
        ),
    ]
    owner: Annotated[
        str,
        Field(
            description="Owner name",
            example="Jane Doe",
            max_length=30,
        ),
    ]
