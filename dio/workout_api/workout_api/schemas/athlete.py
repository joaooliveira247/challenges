from typing import Annotated, Optional

from pydantic import Field, PositiveFloat, PositiveInt

from workout_api.contrib import BaseSchema, OutMixin
from workout_api.schemas.category import CategorySchemaIn
from workout_api.schemas.training_center import TrainingCenterAthlete


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
        str,
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
    category: Annotated[
        CategorySchemaIn,
        Field(description="Athlete Category"),
    ]
    training_center: Annotated[
        TrainingCenterAthlete, Field(description="Athlete training center.")
    ]


class AthletePatchSchema(BaseSchema):
    name: Annotated[
        Optional[str],
        Field(
            None,
            description="Athlete name",
            example="John Doe",
            max_length=50,
        ),
    ]
    age: Annotated[
        Optional[PositiveInt],
        Field(
            None,
            description="Athlete age",
            example=23,
        ),
    ]
    weight: Annotated[
        Optional[PositiveFloat],
        Field(
            None,
            description="Athlete weight in kilograms",
            example=88.5,
        ),
    ]
    height: Annotated[
        Optional[PositiveFloat],
        Field(
            None,
            description="Athlete height in kilograms",
            example=1.75,
        ),
    ]


class AthleteSchemaIn(AthleteSchema): ...


class AthleteSchemaOut(AthleteSchema, OutMixin): ...


class NewAthleteSchemaOut(BaseSchema):
    name: Annotated[
        str,
        Field(
            description="Athlete name",
            example="John Doe",
            max_length=50,
        ),
    ]
    category: Annotated[
        CategorySchemaIn,
        Field(description="Athlete Category"),
    ]
    training_center: Annotated[
        TrainingCenterAthlete, Field(description="Athlete training center.")
    ]
