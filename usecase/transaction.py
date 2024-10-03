from .bases import ITransaction
from models.models import Account


class DepositCommand(ITransaction):
    def __init__(self, account: Account, amount: float):
        self.account = account
        self.amount = amount
    
    def execute(self) -> None:
        self.account.deposit(self.amount)
    
    
class WithdrawCommand(ITransaction):
    def __init__(self, account: Account, amount: float):
        self.account = account
        self.amount = amount
    
    def execute(self) -> None:
        self.account.withdraw(self.amount)


class Transaction:
    def __init__(self):
        self.transaction = None
        
    def set_transaction(self, transaction: ITransaction):
        self.transaction = transaction
        
    def make_transaction(self) -> None:
        if self.transaction:
            self.transaction.execute()
    