from fastapi import APIRouter

from bank_api.controllers.accounts import accounts_controller

api_router = APIRouter()
api_router.include_router(accounts_controller, prefix="/account")
