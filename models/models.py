from pydantic import BaseModel, Field


class Account(BaseModel):
    account_id: str
    customer_id: str
    account_number: str
    balance: float = Field(default=0.0)
    record: list[str] = Field(default=None)
    
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        self.balance += amount
        self._track_transaction(amount, "DEPOSITED")
    
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if self.balance < amount:
            raise ValueError("Insufficient funds!")

        self.balance -= amount
        self._track_transaction(amount, "WITHDRAWN")
    
    def get_balance(self) -> float:
        return self.balance
    
    def _track_transaction(self, amount: float, transaction: str) -> None:
        # Check to see if there is no transactions to the account
        # Initialize an empty list for tracking transactions
        if self.record is None:
            self.record = []
            
        self.record.append(f"Account has {transaction} amount of {amount}")            


class Customer(BaseModel):
    customer_id: str
    name: str
    email: str              # Add email validation
    phone_number: str       # Add phone number validation
    