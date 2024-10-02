from random import randint
from models.models import Account, Customer
from usecase.transaction import DepositCommand, WithdrawCommand
from usecase.account_statement import AccountStatement
from infrastructure.account_repository import AccountFactory, AccountRepository


def main():
    account_repo = AccountRepository()
    
    customer_list: list[Customer] = [
        Customer(
            customer_id="CUST-123", 
            name="Rommel", 
            email="test1@example.com", 
            phone_number="09079090310"
        ),
        Customer(
            customer_id="CUST-456", 
            name="Marlon", 
            email="test2@example.com", 
            phone_number="09999999999"
        ),
        Customer(
            customer_id="CUST-789", 
            name="Maria", 
            email="test3@example.com", 
            phone_number="0111111111"
        ),
        Customer(
            customer_id="CUST-001", 
            name="Rudy", 
            email="test4@example.com", 
            phone_number="09294421213"
        ),
        Customer(
            customer_id="CUST-003", 
            name="RR", 
            email="test5@example.com", 
            phone_number="09089990312"
        ),
    ]
    
    account_list: list[Account] = []
    
    for i, customer in enumerate(customer_list):
        account_list.append(
            AccountFactory.create_account(
                customer,
                "".join(f"000-0{i}")
            )
        )
    
    for account in account_list:
        account_repo.save_account(account)
    
    for a_num, account in account_repo.accounts.items():
        print(f"{a_num} : {account}")
    
    
    assert account_repo.find_account_by_id("ACC-CUST-123-000-00")
    assert account_repo.find_account_by_id("ACC-CUST-456-000-01")
    assert account_repo.find_account_by_id("ACC-CUST-789-000-02")
    assert account_repo.find_account_by_id("ACC-CUST-001-000-03")
    assert account_repo.find_account_by_id("ACC-CUST-003-000-04")
    
    
    
if __name__ == '__main__':
    main()
    