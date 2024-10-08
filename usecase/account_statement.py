from models.models import Account


class AccountStatement:
    def __init__(self, account: Account):
        self.account = account
    
    def generate_account_statement(self) -> str:
        return "\n".join(self.account.record)
    