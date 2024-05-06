from workout_api.contrib import BaseSchema
from typing import Annotated
from pydantic import Field, UUID4


class TrainingCenterSchemaIn(BaseSchema):
    name: Annotated[
        str,
        Field(
            description="Training center name",
            example="Thunder Bird",
            max_length=20,
        ),
    ]
    address: Annotated[
        str,
        Field(
            description="Training center address",
            example="495 Grove Street",
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


class TrainingCenterAthlete(BaseSchema):
    name: Annotated[
        str,
        Field(
            description="Training center name",
            example="Thunder bird",
            max_length=20,
        ),
    ]


class TrainingCenterSchemaOut(TrainingCenterSchemaIn):
    id: Annotated[UUID4, Field(description="ID Training Center")]
