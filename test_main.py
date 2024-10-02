import pytest
from models.models import Account, Customer
from infrastructure.account_repository import AccountFactory, AccountRepository
from usecase.transaction import DepositCommand, WithdrawCommand, Transaction
from usecase.account_statement import AccountStatement


@pytest.fixture
def setup_account():
    customer = Customer(customer_id="CUST-001", name="Alice", email="alice@example.com", phone_number="123-456-7890")
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



# Additional tests can be added here

if __name__ == "__main__":
    pytest.main()
