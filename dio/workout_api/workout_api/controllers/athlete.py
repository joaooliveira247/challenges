from typing import Annotated
from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, Query, status
from fastapi_pagination import LimitOffsetPage, paginate
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from workout_api.core import DatabaseDependency
from workout_api.models import AthleteModel, CategoryModel, TrainingCenterModel
from workout_api.schemas import (
    AthletePatchSchema,
    AthleteSchemaIn,
    AthleteSchemaOut,
    NewAthleteSchemaOut,
)

athlete_controller = APIRouter()


@athlete_controller.post(
    "/",
    summary="Create new athlete.",
    status_code=status.HTTP_201_CREATED,
    response_model=AthleteSchemaOut,
)
async def post(
    db_session: DatabaseDependency, athlete_in: AthleteSchemaIn = Body(...)
) -> AthleteSchemaOut:
    athlete_out = AthleteSchemaOut(
        id=uuid4(),
        **athlete_in.model_dump(),
    )

    category = (
        (
            await db_session.execute(
                select(CategoryModel).filter(
                    CategoryModel.name == athlete_in.category.name
                )
            )
        )
        .scalars()
        .first()
    )
    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category not found in name: {athlete_in.category.name}",
        )

    training_center = (
        (
            await db_session.execute(
                select(TrainingCenterModel).filter(
                    TrainingCenterModel.name == athlete_in.training_center.name
                )
            )
        )
        .scalars()
        .first()
    )
    if not training_center:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Training Center not found in name: {}".format(
                athlete_in.training_center.name
            ),
        )

    athlete_model = AthleteModel(
        **athlete_out.model_dump(
            exclude={"category", "training_center"},
        )
    )
    athlete_model.category_id = category.pk_id
    athlete_model.training_center_id = training_center.pk_id

    try:
        db_session.add(athlete_model)

        await db_session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail="ssn already exists in database.",
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error when try insert data on database.",
        )

    return athlete_out


@athlete_controller.get(
    "/all",
    summary="Get all athletes.",
    status_code=status.HTTP_200_OK,
    response_model=LimitOffsetPage[NewAthleteSchemaOut],
)
async def query(db_session: DatabaseDependency) -> LimitOffsetPage[NewAthleteSchemaOut]:
    athletes: list[NewAthleteSchemaOut] = (
        (await db_session.execute(select(AthleteModel))).scalars().all()
    )

    return paginate(athletes)


@athlete_controller.get(
    "/{id}",
    summary="Get athlete by id.",
    status_code=status.HTTP_200_OK,
    response_model=AthleteSchemaOut,
)
async def query_id(id: UUID4, db_session: DatabaseDependency) -> AthleteSchemaOut:
    athlete: AthleteModel = (
        (await db_session.execute(select(AthleteModel).filter_by(id=id)))
        .scalars()
        .first()
    )
    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Athlete not found in id: {id}",
        )
    return athlete


@athlete_controller.get(
    "/",
    summary="Return athletes by name or ssn",
    status_code=status.HTTP_200_OK,
    response_model=list[AthleteSchemaOut] | AthleteSchemaOut,
)
async def query_parameter(
    db_session: DatabaseDependency,
    name: Annotated[str | None, Query(max_length=50)] = None,
    ssn: Annotated[str | None, Query(max_length=11)] = None,
) -> list[AthleteSchemaOut] | AthleteSchemaOut:

    athlete_ssn = (
        (await db_session.execute(select(AthleteModel).filter_by(ssn=ssn)))
        .scalars()
        .first()
    )
    if athlete_ssn:
        return athlete_ssn
    athlete_name = (
        (
            (
                await db_session.execute(
                    select(AthleteModel).filter(AthleteModel.name.icontains(name))
                )
            )
        )
        .scalars()
        .all()
    )
    return athlete_name


@athlete_controller.patch(
    "/{id}",
    summary="Edit athlete by id.",
    status_code=status.HTTP_200_OK,
    response_model=AthleteSchemaOut,
)
async def update_query_id(
    id: UUID4,
    db_session: DatabaseDependency,
    athlete_patch: AthletePatchSchema = Body(...),
) -> AthleteSchemaOut:
    athlete: AthleteModel = (
        (await db_session.execute(select(AthleteModel).filter_by(id=id)))
        .scalars()
        .first()
    )
    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Athlete not found in id: {id}",
        )
    athlete_update = athlete_patch.model_dump(exclude_unset=True)
    for k, v in athlete_update.items():
        setattr(athlete, k, v)

    await db_session.commit()
    await db_session.refresh(athlete)

    return athlete


@athlete_controller.delete(
    "/{id}",
    summary="delete athlete by id.",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def query_id(id: UUID4, db_session: DatabaseDependency) -> None:
    athlete: AthleteModel = (
        (await db_session.execute(select(AthleteModel).filter_by(id=id)))
        .scalars()
        .first()
    )
    if not athlete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Athlete not found in id: {id}",
        )
    await db_session.delete(athlete)
    await db_session.commit()
    return
