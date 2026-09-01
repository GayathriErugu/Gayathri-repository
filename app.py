class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def display(self):
        print("\nAccount Number :", self.account_number)
        print("Account Holder :", self.holder_name)
        print("Balance        :", self.balance)


accounts = {}


def create_account():
    account_number = input("Enter Account Number: ")
    holder_name = input("Enter Account Holder Name: ")

    try:
        balance = float(input("Enter Initial Balance: "))

        if balance < 0:
            print("Balance cannot be negative.")
            return

        accounts[account_number] = BankAccount(
            account_number,
            holder_name,
            balance
        )

        print("Account created successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def find_account():
    account_number = input("Enter Account Number: ")
    account = accounts.get(account_number)

    if account is None:
        print("Account not found.")

    return account


def deposit_money():
    account = find_account()

    if account:
        try:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        except ValueError:
            print("Invalid amount.")


def withdraw_money():
    account = find_account()

    if account:
        try:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        except ValueError:
            print("Invalid amount.")


def display_account():
    account = find_account()

    if account:
        account.display()


def main():
    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            deposit_money()

        elif choice == "3":
            withdraw_money()

        elif choice == "4":
            display_account()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


main()
