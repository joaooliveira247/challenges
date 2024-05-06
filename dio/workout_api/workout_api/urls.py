from fastapi import APIRouter

from workout_api.controllers import athlete_controller, category_controller

api_router = APIRouter()
api_router.include_router(
    athlete_controller,
    prefix="/athlete",
    tags=["athletes/"],
)
api_router.include_router(
    category_controller,
    prefix="/category",
    tags=["category/"],
)
