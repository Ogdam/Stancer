from src.model import BankAccount, CustomerAccount
from src.StancerClient import StancerClient

clientList = [
    {"username": "agribard", "password": "222222"},
]


def main():
    for client in clientList:
        stancer_client = StancerClient(
            username=client["username"], password=client["password"]
        )

        identity = stancer_client.identity()
        stancer_bank_accounts = []

        for account in stancer_client.accounts():
            balaces = stancer_client.balance(account.id)
            transactions = stancer_client.transaction(account.id)
            stancer_bank_accounts.append(BankAccount(account, balaces, transactions))

        stancer_customer_account = CustomerAccount(identity, stancer_bank_accounts)

        print(stancer_customer_account.identity)
        for ba in stancer_customer_account.bank_account_list:
            print(ba.account)
            for b in ba.balance:
                print(b)
            for c in ba.transaction_list:
                print(c)


if __name__ == "__main__":
    main()
