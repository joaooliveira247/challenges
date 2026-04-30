from fastapi import APIRouter, HTTPException, status
from sqlalchemy import func

from bank_api.contrib.errors import DatabaseError, UnexpectedError
from bank_api.dependencies.auth import CurrentAccount
from bank_api.dependencies.database import DatabaseDependency
from bank_api.models.transaction import (
    TransactionModel,
    TransactionStatusEnum,
    TransactionTypeEnum,
)
from bank_api.repositories.accounts import AccountsRepository
from bank_api.repositories.transactions import TransactionsRepository
from bank_api.schemas.response import Money

transactions_controller = APIRouter(tags=["transaction"])


@transactions_controller.post("/deposit")
async def deposit(
    db: DatabaseDependency, account: CurrentAccount, amount: Money
) -> Money:
    transactions_repository = TransactionsRepository(db)
    accounts_repository = AccountsRepository(db)

    amount_cents = int(amount * 100)

    new_balance = account.balance + amount_cents

    transaction = TransactionModel(
        account_id=account.id,
        amount=amount_cents,
        balance_after=new_balance,
        status=TransactionStatusEnum.ACCEPT,
        type=TransactionTypeEnum.DEPOSIT,
    )

    try:
        await accounts_repository.update_balance(
            account_id=account.id,
            amount=new_balance,
        )

        await transactions_repository.create(transaction)

        return new_balance

    except (DatabaseError, UnexpectedError) as e:
        transaction.status = TransactionStatusEnum.REFUND

        await transactions_repository.create(transaction)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


transactions_controller.post("/withdrawal")


async def withdrawal(
    db: DatabaseDependency,
    account: CurrentAccount,
    amount: Money,
) -> Money:
    transactions_repository = TransactionsRepository(db)
    accounts_repository = AccountsRepository(db)

    amount_cents = int(amount * 100)

    if account.balance < amount_cents:
        transaction = TransactionModel(
            account_id=account.id,
            amount=amount_cents,
            balance_after=account.balance,
            status=TransactionStatusEnum.REFUND,
            type=TransactionTypeEnum.WITHDRAWAL,
        )

        await transactions_repository.create(transaction)

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient balance",
        )

    new_balance = account.balance - amount_cents

    transaction = TransactionModel(
        account_id=account.id,
        amount=amount_cents,
        balance_after=new_balance,
        status=TransactionStatusEnum.ACCEPT,
        type=TransactionTypeEnum.WITHDRAWAL,
    )

    try:
        await accounts_repository.update_balance(
            account_id=account.id,
            amount=new_balance,
        )

        await transactions_repository.create(transaction)

        return new_balance

    except (DatabaseError, UnexpectedError) as e:
        transaction.status = TransactionStatusEnum.REFUND

        await transactions_repository.create(transaction)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
