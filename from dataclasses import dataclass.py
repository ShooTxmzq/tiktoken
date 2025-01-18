from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List

class Category(Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    TRANSFER = "TRANSFER"

@dataclass
class Transaction:
    amount: Decimal
    category: Category
    description: str
    date: datetime = datetime.now()

    def __post_init__(self):
        if not isinstance(self.amount, Decimal):
            self.amount = Decimal(str(self.amount))
        if self.amount <= 0:
            raise ValueError("Amount must be positive")

class Account:
    def __init__(self, initial_balance: Decimal = Decimal('0')):
        self.balance = initial_balance
        self.transactions: List[Transaction] = []
    
    def add_transaction(self, amount: Decimal, category: Category, description: str) -> None:
        transaction = Transaction(amount, category, description)
        if category == Category.EXPENSE:
            if self.balance < amount:
                raise ValueError("Insufficient funds")
            self.balance -= amount
        else:
            self.balance += amount
        self.transactions.append(transaction)
    
    def get_balance(self) -> str:
        return f"${self.balance:,.2f}"
    
    def get_history(self) -> List[str]:
        return [
            f"{t.date:%Y-%m-%d} | {t.category.value:8} | ${t.amount:10,.2f} | {t.description}"
            for t in self.transactions
        ]
