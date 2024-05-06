from fastapi import APIRouter

from workout_api.controllers import (
    athlete_controller,
    category_controller,
    training_center_controller,
)

api_router = APIRouter()
api_router.include_router(
    athlete_controller,
    prefix="/athlete",
    tags=["Athletes"],
)
api_router.include_router(
    category_controller,
    prefix="/category",
    tags=["Categories"],
)
api_router.include_router(
    training_center_controller,
    prefix="/training_center",
    tags=["Training Centers"],
)
