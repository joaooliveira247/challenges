from pydantic import BaseModel, Field, PositiveInt, PositiveFloat
from typing import Annotated


class AthleteSchema(BaseModel):
    name: Annotated[
        str,
        Field(
            description="Athlete name",
            examples="John Doe",
            max_length=50,
        ),
    ]
    ssn: Annotated[
        PositiveInt,
        Field(
            description="Social Security Number",
            examples="12345678900",
            max_length=11,
        ),
    ]
    age: Annotated[
        PositiveInt,
        Field(
            description="Athlete age",
            examples=23,
        ),
    ]
    weight: Annotated[
        PositiveFloat,
        Field(
            description="Athlete weight in kilograms",
            examples=88.5,
        ),
    ]
    height: Annotated[
        PositiveFloat,
        Field(
            description="Athlete height in kilograms",
            examples=1.75,
        ),
    ]
    sex: Annotated[
        str,
        Field(
            description="Sex",
            examples=["M - Man", "W - Woman"],
            max_length=1,
        ),
    ]
