from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from workout_api.core import DatabaseDependency
from workout_api.models import CategoryModel
from workout_api.schemas import CategorySchemaIn, CategorySchemaOut

category_controller = APIRouter()


@category_controller.post(
    "/",
    summary="Create new category.",
    status_code=status.HTTP_201_CREATED,
    response_model=CategorySchemaOut,
)
async def post(
    db_session: DatabaseDependency, category_in: CategorySchemaIn = Body(...)
) -> CategorySchemaOut:
    category_out = CategorySchemaOut(id=uuid4(), **category_in.model_dump())
    category_model = CategoryModel(**category_out.model_dump())

    try:
        db_session.add(category_model)

        await db_session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail="Category already exists in database.",
        )

    return category_out


@category_controller.get(
    "/",
    summary="Get all categories.",
    status_code=status.HTTP_200_OK,
    response_model=list[CategorySchemaOut],
)
async def query(db_session: DatabaseDependency) -> list[CategorySchemaOut]:
    categories: list[CategorySchemaOut] = (
        (await db_session.execute(select(CategoryModel))).scalars().all()
    )
    return categories


@category_controller.get(
    "/{id}",
    summary="Get category by id.",
    status_code=status.HTTP_200_OK,
    response_model=CategorySchemaOut,
)
async def query_id(id: UUID4, db_session: DatabaseDependency) -> CategorySchemaOut:
    category: CategorySchemaOut = (
        (await db_session.execute(select(CategoryModel).filter_by(id=id)))
        .scalars()
        .first()
    )
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category not found in id: {id}",
        )
    return category
