# 🏦 Bank Account System

A command line banking application that manages accounts, deposits, withdrawals, and transfers. Built in Python using object-oriented programming.

---

## 📋 Overview

This app simulates a basic banking system where you can create accounts, deposit and withdraw money, transfer between accounts, and view full transaction histories. All data is saved to a JSON file so nothing is lost when you close the app.

---

## 📁 Project Structure

```
bank-account-system/
│
├── src/
│   ├── __init__.py
│   ├── account.py        # Account class
│   ├── bank.py           # Bank class (manages all accounts)
│   └── transaction.py    # Transaction class (records every action)
│
├── data/
│   └── bank.json         # Saved account data
│
├── main.py               # Entry point / menu
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/GPannu77/bank-account-system.git
cd bank-account-system
```

**2. Run the app**
```bash
python main.py
```

No external libraries needed — just Python 3!

---

## ✨ Features

- Create and delete bank accounts
- Deposit and withdraw money
- Transfer funds between accounts
- View full transaction history per account
- Handles errors like insufficient funds
- Saves and loads data from JSON automatically

---

## 🧱 How It's Built

| File | Class | Responsibility |
|---|---|---|
| account.py | `Account` | Stores owner, balance, and transaction history |
| transaction.py | `Transaction` | Records every action with amount, type, and date |
| bank.py | `Bank` | Manages all accounts, handles transfers, saves/loads data |

---

## 📊 Example Output

```
==== Bank Account System ====
1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. View Transaction History
6. Exit

Enter choice: 5

Account: Alice Johnson (ACC001)
Balance: $1,250.00
Transactions:
  [2026-04-01] DEPOSIT    + $500.00
  [2026-04-03] WITHDRAWAL - $250.00
  [2026-04-05] TRANSFER   - $100.00
  [2026-04-10] DEPOSIT    +$1,100.00
```

---

## 🛠️ Technologies Used

- **Python 3**
- **JSON** — for data storage
- **OOP** — classes and methods throughout
- **datetime** — for timestamping transactions

---

## 👤 Author

Gurnoor Pannu — [GitHub](https://github.com/GPannu77)