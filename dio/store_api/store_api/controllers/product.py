from fastapi import APIRouter, status, Body, Depends
from store_api.schemas.products import ProductIn, ProductOut
from store_api.usecases.product import ProductUseCase

product_controller = APIRouter(tags=["products"])


@product_controller.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ProductIn = Body(...),
    usecase: ProductUseCase = Depends(),
) -> ProductOut:
    return await usecase.create(body=body)
