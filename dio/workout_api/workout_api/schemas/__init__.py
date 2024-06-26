from workout_api.schemas.athlete import (
    AthleteSchemaIn,
    AthleteSchemaOut,
    AthletePatchSchema,
    NewAthleteSchemaOut,
)
from workout_api.schemas.category import CategorySchemaIn, CategorySchemaOut
from workout_api.schemas.training_center import (
    TrainingCenterSchemaIn,
    TrainingCenterSchemaOut,
    TrainingCenterAthlete,
)


__all__ = [
    "AthletePatchSchema",
    "AthleteSchemaIn",
    "AthleteSchemaOut",
    "NewAthleteSchemaOut",
    "CategorySchemaIn",
    "CategorySchemaOut",
    "TrainingCenterAthlete",
    "TrainingCenterSchemaIn",
    "TrainingCenterSchemaOut",
]
