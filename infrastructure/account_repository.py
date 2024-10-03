from typing import Optional
from models.models import Account, Customer


class AccountFactory:
    @staticmethod
    def create_account(customer: Customer, account_number: str) -> Account:
        account_id = f"ACC-{customer.customer_id}-{account_number}"
        return Account(account_id=account_id, customer_id=customer.customer_id, account_number=account_number)


class AccountRepository:
    def __init__(self):
        self._accounts = {}
    
    def save_account(self, account: Account):
        self.accounts[account.customer_id] = account

    def find_account_by_id(self, account_id: str) -> Optional[Account]:
        for account in self.accounts.values():
            if account.account_id == account_id:
                return account
    
    def find_accounts_by_customer_id(self, customer_id: str) -> list[Account]:
        return [
            account 
            for account in self.accounts.values()
            if account.customer_id == customer_id
        ]
    
    @property
    def accounts(self) -> dict:
        return self._accounts
    