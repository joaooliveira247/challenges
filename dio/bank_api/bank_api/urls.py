from fastapi import APIRouter

from bank_api.controllers.accounts import accounts_controller
from bank_api.core.config import get_settings

settings = get_settings()

api_router = APIRouter(prefix=settings.API_PATH)
api_router.include_router(accounts_controller, prefix="/account")
