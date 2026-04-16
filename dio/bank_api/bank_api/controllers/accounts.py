from fastapi import Body, status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from bank_api.contrib.errors import DatabaseError, UnexpectedError
from bank_api.core.security import gen_hash
from bank_api.dependencies.database import DatabaseDependency
from bank_api.models.accounts import AccountModel
from bank_api.repositories.accounts import AccountsRepository
from bank_api.schemas.accounts import AccountInSchema
from bank_api.schemas.response import AccountCreatedSchema

accounts_controller = APIRouter(tags=["account"])


@accounts_controller.post("/sign-up", status_code=status.HTTP_201_CREATED)
async def create_account(
    db: DatabaseDependency,
    body: AccountInSchema = Body(...),
) -> AccountCreatedSchema:
    repository: AccountsRepository = AccountsRepository(db)

    account = AccountModel(**body.model_dump())

    try:
        account_hashed_password = gen_hash(account.password)
        account.password = account_hashed_password
        account_id = await repository.create(account)
        return AccountCreatedSchema(id=account_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=str(e)
        )
    except DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
    except UnexpectedError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
