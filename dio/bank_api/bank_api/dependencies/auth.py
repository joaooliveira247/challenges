from __future__ import annotations

from tokenize import TokenError
from typing import Annotated, Any

from fastapi import Depends, HTTPException, status

from bank_api.contrib.errors import DatabaseError, UnexpectedError
from bank_api.core.token import verify_token_jwt
from bank_api.dependencies.database import DatabaseDependency
from bank_api.dependencies.token import TokenDependency
from bank_api.models.accounts import AccountModel
from bank_api.repositories.accounts import AccountsRepository
from bank_api.schemas.accounts import AccountOutSchema

CurrentAccount = Annotated[AccountOutSchema, Depends(get_current_user)]


async def get_current_user(
    db: DatabaseDependency, token: TokenDependency
) -> AccountModel:
    credencial_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload: dict[str, Any] | None = verify_token_jwt(token)

        if payload is None or (account_id := payload["sub"]) is None:
            raise credencial_exception

        account_repository = AccountsRepository(db)

        account = await account_repository.get_account_by_id(account_id)

        if account is None:
            credencial_exception.detail = "Account can't be authenticated"
            raise credencial_exception

        return account
    except (TokenError, DatabaseError) as e:
        credencial_exception.detail = str(e)
        raise credencial_exception

    except UnexpectedError as e:
        credencial_exception.detail = str(e)
        raise credencial_exception
