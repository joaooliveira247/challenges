from tokenize import TokenError

from fastapi import Body, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from bank_api.contrib.errors import (
    DatabaseError,
    InvalidResource,
    UnexpectedError,
)
from bank_api.core.auth import authenticate
from bank_api.core.security import gen_hash
from bank_api.core.token import gen_jwt
from bank_api.dependencies.auth import CurrentAccount
from bank_api.dependencies.database import DatabaseDependency
from bank_api.models.accounts import AccountModel
from bank_api.repositories.accounts import AccountsRepository
from bank_api.schemas.accounts import AccountInSchema, AccountOutSchema
from bank_api.schemas.response import (
    AccountCreatedSchema,
    AccountTokenResponse,
)

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


@accounts_controller.post("/sign-up", status_code=status.HTTP_200_OK)
async def login(
    db: DatabaseDependency, form_data: OAuth2PasswordRequestForm = Depends()
) -> AccountTokenResponse:
    try:
        account = await authenticate(
            db, form_data.username, form_data.password
        )

        jwt = gen_jwt(account)

        return AccountTokenResponse(access_token=jwt)
    except (DatabaseError, TokenError) as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
    except InvalidResource as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
    except UnexpectedError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@accounts_controller.get("/", status_code=status.HTTP_200_OK)
async def get_current_account(account: CurrentAccount) -> AccountOutSchema:
    return account


@accounts_controller.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db: DatabaseDependency, account: CurrentAccount) -> None:
    account_repository = AccountsRepository(db)

    try:
        account_db = await account_repository.get_account_by_query(
            ssn=account.ssn
        )

        if account_db is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Account not found, try refresh your authenticaion token.",
            )

        await account_repository.delete_account(account_db.id)

        return None

    except DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
    except UnexpectedError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
