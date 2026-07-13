#Defining the class
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
    
        if amount <= 0:
            print("Withdrawal amount must be positive")

        elif amount > self.balance:
            print("Insufficient funds.")

        else:
            self.balance -= amount
            print(f"Withdrew Ksh {amount}")

    def display_balance(self):
        print(f"{self.owner}'s Balance: Ksh{self.balance}")


# Create an object
account = BankAccount("Larry", 1000)

# Use the object's methods
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()