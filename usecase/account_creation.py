from models.models import Account, Customer


class AccountFactory:
    @staticmethod
    def create_account(customer: Customer, account_number: str) -> Account:
        account_id = f"ACC-{customer.customer_id}-{account_number}"
        return Account(account_id=account_id, customer_id=customer.customer_id, account_number=account_number)
