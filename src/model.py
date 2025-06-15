from dataclasses import dataclass
from datetime import datetime


@dataclass
class Identity:
    id: str
    prefix: str
    first_name: str
    last_name: str
    date_of_birth: str


@dataclass
class Account:
    id: str
    type: str
    usage: str
    iban: str
    name: str
    currency: str


@dataclass
class Balance:
    id: str
    name: str
    amount: int
    currency: str
    type: str


@dataclass
class Transaction:
    id: str
    label: str
    amount: int
    crdt_dbit_indicator: str
    status: str
    currency: str
    date_operation: datetime
    date_processed: datetime

    def __post_init__(self):
        if isinstance(self.date_operation, str):
            self.date_operation = datetime.fromisoformat(self.date_operation)
        if isinstance(self.date_processed, str):
            self.date_processed = datetime.fromisoformat(self.date_processed)


@dataclass
class BankAccount:
    account: Account
    balance: list[Balance]
    transaction_list: list[Transaction]


@dataclass
class CustomerAccount:
    identity: Identity
    bank_account_list: list[BankAccount]
