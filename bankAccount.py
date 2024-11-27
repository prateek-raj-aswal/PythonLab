class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")
        else:
            raise ValueError("Insufficient balance.")

# Test the class
account = BankAccount(12345, "John Doe")
account.deposit(500)
account.withdraw(200)

try:
    account.withdraw(400)
except ValueError as e:
    print(e)
