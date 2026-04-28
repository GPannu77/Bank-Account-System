from src.transaction import Transaction

class Account:
    def __init__(self, account_number, holder):
        self.account_number = account_number
        self.holder = holder
        self.balance = 0.0
        self.transactions = []
    
    def deposit(self, amount, description):
        if amount <= 0:
            return "Error: Deposit amount must be positive."
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount, description))
    
    def withdraw(self, amount, description):
        if amount <= 0:
            return "Error: Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.transactions.append(Transaction("Withdrawal", amount, description))
    
    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transactions
    
    def to_dict(self):
        return {
            "Account Number": self.account_number,
            "Holder Name": self.holder,
            "Balance": self.balance,
            "Transactions": [t.to_dict() for t in self.transactions]
        }
    
    def __str__(self):
        return f"Account: {self.holder} ({self.account_number}) | Balance: ${self.balance:.2f}"