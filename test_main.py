import pytest
from models.models import Customer
from infrastructure.account_repository import AccountFactory, AccountRepository
from usecase.transaction import DepositCommand, WithdrawCommand, Transaction
from usecase.account_statement import AccountStatement


@pytest.fixture
def setup_account():
    customer = Customer(customer_id="CUST-001", name="Rommel", email="rommeldm87@example.com", phone_number="123-456-7890")
    account = AccountFactory.create_account(customer, "123456789")
    return account


def test_initial_balance(setup_account):
    account = setup_account
    assert account.get_balance() == 0.0


def test_deposit(setup_account):
    account = setup_account
    t = Transaction()
    t.set_transaction(DepositCommand(account, 1000.0))
    t.make_transaction()
    assert account.get_balance() == 1000.0


def test_withdraw(setup_account):
    account = setup_account
    t = Transaction()
    t.set_transaction(DepositCommand(account, 1000.0))
    t.make_transaction()
    t.set_transaction(WithdrawCommand(account, 500.0))
    t.make_transaction()
    assert account.get_balance() == 500.0


def test_withdraw_insufficient_funds(setup_account):
    account = setup_account
    t = Transaction()
    t.set_transaction(DepositCommand(account, 500.0))
    t.make_transaction()
    with pytest.raises(ValueError, match="Insufficient funds!"):
        t.set_transaction(WithdrawCommand(account, 501.0))
        t.make_transaction()
    
    
def test_deposit_negative_amount(setup_account):
    account = setup_account
    t = Transaction()
    with pytest.raises(ValueError, match="Amount must be positive"):
        t.set_transaction(DepositCommand(account, -200.0))
        t.make_transaction()


def test_get_account_statement(setup_account):
    account = setup_account
    t = Transaction()
    
    deposit_amount = 10_000.0
    withdraw_amount = 5000.0
    
    t.set_transaction(DepositCommand(account, deposit_amount))
    t.make_transaction()
    t.set_transaction(WithdrawCommand(account, withdraw_amount))
    t.make_transaction()
    
    acs = AccountStatement(account)
    account_statement = f"Account has DEPOSITED amount of {deposit_amount}\nAccount has WITHDRAWN amount of {withdraw_amount}"
    
    assert acs.get_account_statement() == account_statement
    

def test_save_account(setup_account):
    account = setup_account
    acc_repo = AccountRepository()

    acc_repo.save_account(account)
    
    account_ids = {acc.account_id for acc in acc_repo.accounts.values()}

    assert account.account_id in account_ids


def test_find_accounts_by_id(setup_account):
    account = setup_account
    acc_repo = AccountRepository()

    acc_repo.save_account(account)
    
    assert account == acc_repo.find_account_by_id(account.account_id)


def test_find_accounts_by_customer_id(setup_account):
    account = setup_account
    acc_repo = AccountRepository()
    
    acc_repo.save_account(account)
    
    account_list = acc_repo.find_accounts_by_customer_id(account.customer_id)

    assert account in account_list


if __name__ == "__main__":
    pytest.main()
