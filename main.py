from src.bank import Bank


def print_menu():
    print("==== Bank Account System ====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. View Balance")
    print("6. View Transaction History")
    print("7. Exit")


def main():
    bank = Bank()
    
    try:
        bank.load_data("bank_data.json")
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found, starting fresh.")
        
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter account holder's name: ")
            bank.create_account(name)
        elif choice == "2":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to be deposited: "))
            bank.deposit(acc_num, amount, "Deposit")
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to be withdrawn: "))
            bank.withdraw(acc_num, amount, "Withdrawal")
        elif choice == "4":
            from_acc = input("Enter source account number: ")
            to_acc = input("Enter destination account number: ")
            amount = float(input("Enter amount to be transferred: "))
            bank.transfer(from_acc, to_acc, amount)
        elif choice == "5":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account is not None:
                print(f"Current balance: ${account.get_balance():.2f}")
        elif choice == "6":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account is not None:
                print("Transaction History:")
                for t in account.get_transaction_history():
                    print(f"{t.date} - {t.transaction_type}: ${t.amount:.2f} / {t.description}")
        elif choice == "7":
            try:
                bank.save_data("bank_data.json")
                print("Data saved. Exiting.")
            except FileNotFoundError:
                print("Error saving data. Exiting without saving.")
            break
        else:
            print("Invalid choice.")
        
        print()


if __name__ == "__main__":
    main()
