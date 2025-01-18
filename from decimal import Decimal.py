from decimal import Decimal
from models.money import Account, Category

def test_account():
    account = Account(Decimal('1000'))
    account.add_transaction(Decimal('500'), Category.INCOME, "Salary")
    account.add_transaction(Decimal('100'), Category.EXPENSE, "Groceries")
    
    assert account.get_balance() == "$1,400.00"
    assert len(account.get_history()) == 2
