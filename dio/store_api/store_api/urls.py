from fastapi import APIRouter
from store_api.controllers.product import product_controller

api_router = APIRouter()
api_router.include_router(product_controller, prefix="/products")
