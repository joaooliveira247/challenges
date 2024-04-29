from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime


class Account:
    def __init__(self, number: int, client: Client) -> None:
        self.balance: float = 0
        self._number = number
        self._office = "0001"
        self._client = client
        self.history = History()

    @classmethod
    def new(cls, client: Client, number: int) -> Account:
        return cls(number, client)

    @property
    def balance(self) -> float:
        return self.balance

    @property
    def number(self) -> int:
        return self._number

    @property
    def office(self) -> str:
        return self.office

    @property
    def client(self) -> Client:
        return self._client

    @property
    def history(self) -> History:
        return self.history

    def draw(self, value: float) -> None | bool:
        if value > self.balance:
            print("Invalid operation")
            return
        if value > 0:
            self.saldo -= value
            print("USD {value} drawee")
            return True
        print("Invalid operation")
        return False

    def deposit(self, value: float) -> bool:
        if value > 0:
            self.balance += value
            print("USD {value} deposited")
            return True
        print("Invalid operation")
        return False


class CheckingAccount(Account):
    def __init__(
        self,
        number: int,
        client: Client,
        limit: float = 500,
        limit_draw: int = 3,
    ) -> None:
        super().__init__(number, client)
        self.limit = limit
        self.limit_draw = limit_draw

    def draw(self, value: float) -> bool:
        num_draws: int = len(
            [
                transaction
                for transaction in self.history.transactions
                if transaction["type_"] == Draw.__name__
            ]
        )

        if value > self.limit:
            print("Invalid Operation")
            return False
        if num_draws > self.limit_draw:
            print("Invalid Operation")
            return False
        return self.draw(value)


class History:
    def __init__(self) -> None:
        self._transactions: list[Transaction] = []

    @property
    def trasactions(self) -> list:
        return self._transactions

    def add_transaction(self, transaction: Transaction) -> None:
        self.trasactions.append(
            {
                "type_": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Client:
    def __init__(self, address: str) -> None:
        self.address = address
        self.accounts: list[Account] = []

    def transaction(self, account: Account, transaction: Transaction) -> None:
        transaction.register(account)

    def add_account(self, account: Account) -> None:
        self.accounts.append(account)


class Transaction(ABC):
    @property
    @abstractmethod
    def value(self): ...

    @classmethod
    @abstractmethod
    def register(self, account: Account): ...


class Draw(Transaction):
    def __init__(self, value: float) -> None:
        self._value = value

    @property
    def value(self) -> float:
        return self.value

    def register(self, account: Account) -> None:
        transaction = account.draw(self._value)
        if transaction:
            account.history.add_transaction(self)


class Deposit(Transaction):
    def __init__(self, value: float) -> None:
        self._value = value

    @property
    def value(self) -> float:
        return self._value

    def register(self, account: Account) -> None:
        transaction = account.deposit(self._value)

        if transaction:
            account.history.add_transaction(self)


class Individual(Client):
    def __init__(
        self,
        name: str,
        birth_date: datetime,
        cpf: str,
        address: str,
    ) -> None:
        super().__init__(address)
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf
