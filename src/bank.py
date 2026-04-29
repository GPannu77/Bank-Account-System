from src.account import Account
from src.transaction import Transaction
from datetime import datetime
import json


class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1

    def create_account(self, name):
        account_number = f"ACC{self.next_account_number:04d}"
        self.accounts[account_number] = Account(account_number, name)
        self.next_account_number += 1
        print(f"Account created: {account_number} for {name}")

    def get_account(self, account_number):
        if account_number not in self.accounts:
            print("Error: Account not found.")
            return None
        return self.accounts[account_number]

    def deposit(self, account_number, amount, description):
        account = self.get_account(account_number)
        if account is not None:
            account.deposit(amount, description)

    def withdraw(self, account_number, amount, description):
        account = self.get_account(account_number)
        if account is not None:
            account.withdraw(amount, description)

    def transfer(self, from_account, to_account, amount):
        from_acc = self.get_account(from_account)
        to_acc = self.get_account(to_account)
        if from_acc is None or to_acc is None:
            print("Error: one or more accounts not found.")
        else:
            from_acc.withdraw(amount, f"Transfer to {to_account}")
            to_acc.deposit(amount, f"Transfer from {from_account}")

    def save_data(self, filename):
        data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_data(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        for acc_num, acc_data in data.items():
            account = Account(acc_data["Account Number"], acc_data["Holder Name"])
            account.balance = acc_data["Balance"]
            for t in acc_data["Transactions"]:
                transaction = Transaction(t["type"], t["amount"], t["description"])
                transaction.date = datetime.fromisoformat(t["date"])
                account.transactions.append(transaction)
            self.accounts[acc_num] = account

    def __str__(self):
        return f"Bank | Total Accounts: {len(self.accounts)}"
