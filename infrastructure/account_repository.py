from typing import Optional
from models.models import Account

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
    