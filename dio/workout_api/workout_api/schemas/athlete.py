from pydantic import Field, PositiveInt, PositiveFloat
from typing import Annotated

from workout_api.contrib import BaseSchema


class AthleteSchema(BaseSchema):
    name: Annotated[
        str,
        Field(
            description="Athlete name",
            example="John Doe",
            max_length=50,
        ),
    ]
    ssn: Annotated[
        PositiveInt,
        Field(
            description="Social Security Number",
            example="12345678900",
            max_length=11,
        ),
    ]
    age: Annotated[
        PositiveInt,
        Field(
            description="Athlete age",
            example=23,
        ),
    ]
    weight: Annotated[
        PositiveFloat,
        Field(
            description="Athlete weight in kilograms",
            example=88.5,
        ),
    ]
    height: Annotated[
        PositiveFloat,
        Field(
            description="Athlete height in kilograms",
            example=1.75,
        ),
    ]
    sex: Annotated[
        str,
        Field(
            description="Sex",
            example=["M - Man", "W - Woman"],
            max_length=1,
        ),
    ]
