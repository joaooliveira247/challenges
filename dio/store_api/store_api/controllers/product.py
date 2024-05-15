from fastapi import APIRouter, status, Body, Depends, HTTPException, Path
from store_api.schemas.products import ProductIn, ProductOut
from store_api.usecases.product import ProductUseCase
from pydantic import UUID4
from store_api.core.exceptions import DBNotFoundValueException

product_controller = APIRouter(tags=["products"])


@product_controller.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ProductIn = Body(...),
    usecase: ProductUseCase = Depends(),
) -> ProductOut:
    return await usecase.create(body=body)


@product_controller.get(path="/{id}", status_code=status.HTTP_200_OK)
async def get(
    id: UUID4 = Path(...),
    usecase: ProductUseCase = Depends(),
) -> ProductOut:
    try:
        return await usecase.get(id)
    except DBNotFoundValueException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found."
        )


@product_controller.get(
    path="/", status_code=status.HTTP_200_OK, response_model=list[ProductOut]
)
async def query(
    usecase: ProductUseCase = Depends(),
) -> list[ProductOut]:
    return await usecase.query()
