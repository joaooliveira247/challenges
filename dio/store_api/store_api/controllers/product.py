from fastapi import APIRouter, status, Body, Depends, HTTPException, Path, Query
from store_api.schemas.products import (
    ProductIn,
    ProductOut,
    ProductUpdateOut,
    ProductUpdate,
)
from store_api.usecases.product import ProductUseCase
from pydantic import UUID4, PositiveFloat
from store_api.core.exceptions import DBNotFoundValueException, ProductAlreadyExists
from store_api.core.utils import to_decimal

product_controller = APIRouter(tags=["products"])


@product_controller.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ProductIn = Body(...),
    usecase: ProductUseCase = Depends(),
) -> ProductOut:
    try:
        return await usecase.create(body=body)
    except ProductAlreadyExists as err:
        raise HTTPException(
            status.HTTP_406_NOT_ACCEPTABLE,
            err.message,
        )


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
    lt: PositiveFloat | None = Query(None),
    gt: PositiveFloat | None = Query(None),
    usecase: ProductUseCase = Depends(),
) -> list[ProductOut]:
    if gt and lt:
        if gt > lt:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"{lt} > {gt}"
            )
        return await usecase.query_filter(
            {"price": {"$gt": to_decimal(gt), "$lt": to_decimal(lt)}}
        )
    if lt:
        return await usecase.query_filter({"price": {"$lt": to_decimal(lt)}})
    if gt:
        return await usecase.query_filter({"price": {"$gt": to_decimal(gt)}})

    return await usecase.query()


@product_controller.patch(
    path="/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ProductUpdateOut,
)
async def patch(
    id: UUID4 = Path(alias="id"),
    body: ProductUpdate = Body(...),
    usecase: ProductUseCase = Depends(),
) -> ProductUpdateOut:
    try:
        return await usecase.update(id, body=body)
    except DBNotFoundValueException:
        raise HTTPException(
            status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"Product not found at id: {id}",
        )


@product_controller.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID4 = Path(...),
    usecase: ProductUseCase = Depends(),
) -> None:
    try:
        return await usecase.delete(id)
    except DBNotFoundValueException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found."
        )
