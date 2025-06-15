import time
from functools import wraps

from .model import Account, Balance, Identity, Transaction
from .utils import stancer_get_data, stancer_get_token


class StancerClient:

    token_max_lifetime = 3600

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.token = self.__get_token()
        self.token_created = time.time()

    def __get_token(self) -> str:
        return stancer_get_token(
            username=self.username,
            password=self.password,
            grant_type="password",
            client_id="string",
            client_secret="string",
            scope="stet",
        )

    def valid_token(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if (
                self.token is None
                or time.time() - self.token_created >= self.token_max_lifetime
            ):
                self.token = self.__get_token()
            return func(self, *args, **kwargs)

        return wrapper

    @valid_token
    def identity(self) -> Identity:
        data = stancer_get_data(url="stet/identity", token=self.token)
        return Identity(**data)

    @valid_token
    def accounts(self) -> list[Account]:
        accounts = stancer_get_data(url="stet/account", token=self.token)
        return [Account(**account) for account in accounts]

    @valid_token
    def account(self, account_id: str) -> Account:
        account = stancer_get_data(url=f"stet/account/{account_id}", token=self.token)
        return Account(**account)

    @valid_token
    def balance(self, account_id: str) -> list[Balance]:
        balances = stancer_get_data(
            url=f"stet/account/{account_id}/balance", token=self.token
        )
        return [Balance(**balance) for balance in balances]

    @valid_token
    def transaction(self, account_id: str) -> list[Transaction]:
        transactions = stancer_get_data(
            url=f"stet/account/{account_id}/transaction", token=self.token
        )
        return [Transaction(**transaction) for transaction in transactions]
