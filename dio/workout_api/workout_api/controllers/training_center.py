from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from workout_api.core import DatabaseDependency
from workout_api.models import TrainingCenterModel
from workout_api.schemas import TrainingCenterSchemaIn, TrainingCenterSchemaOut

training_center_controller = APIRouter()


@training_center_controller.post(
    "/",
    summary="Create new training center.",
    status_code=status.HTTP_201_CREATED,
    response_model=TrainingCenterSchemaOut,
)
async def post(
    db_session: DatabaseDependency, training_in: TrainingCenterSchemaIn = Body(...)
) -> TrainingCenterSchemaOut:
    training_out = TrainingCenterSchemaOut(
        id=uuid4(),
        **training_in.model_dump(),
    )
    training_model = TrainingCenterModel(**training_out.model_dump())

    try:
        db_session.add(training_model)

        await db_session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail="Training center already exists in database.",
        )

    return training_out


@training_center_controller.get(
    "/",
    summary="Get all training center.",
    status_code=status.HTTP_200_OK,
    response_model=list[TrainingCenterSchemaOut],
)
async def query(db_session: DatabaseDependency) -> list[TrainingCenterSchemaOut]:
    training_centers: list[TrainingCenterSchemaOut] = (
        (await db_session.execute(select(TrainingCenterModel))).scalars().all()
    )
    return training_centers


@training_center_controller.get(
    "/{id}",
    summary="Get training center by id.",
    status_code=status.HTTP_200_OK,
    response_model=TrainingCenterSchemaOut,
)
async def query_id(
    id: UUID4, db_session: DatabaseDependency
) -> TrainingCenterSchemaOut:
    training_center: TrainingCenterSchemaOut = (
        (await db_session.execute(select(TrainingCenterModel).filter_by(id=id)))
        .scalars()
        .first()
    )
    if not training_center:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Training center not found in id: {id}",
        )
    return training_center
