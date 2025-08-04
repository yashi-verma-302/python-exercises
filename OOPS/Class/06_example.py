class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit amount: {amount}")
        else:
            print("Deposit amount can't be negative")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")

# Test the class
acc = BankAccount("Yashi")
acc.deposit(1000)
acc.withdraw(300)
acc.display_balance()