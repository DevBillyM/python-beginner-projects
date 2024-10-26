# Base class for a Bank Account
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. You have {self.balance} in your account.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account.")

    def get_balance(self):
        return self.balance

# Subclass for a Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied {interest} interest to {self.account_holder}'s account.")

# Subclass for a Checking Account
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > (self.balance + self.overdraft_limit):
            print(f"Overdraft limit exceeded. You can withdraw up to {self.balance + self.overdraft_limit}.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account.")

# Example usage
def banking_system():
    # Create a savings account and checking account
    john_savings = SavingsAccount("John Doe", 1000)
    john_checking = CheckingAccount("John Doe", 500)
    
    # Perform operations
    john_savings.deposit(200)
    john_savings.apply_interest()
    print(f"John's savings balance: {john_savings.get_balance()}")

    john_checking.withdraw(600)
    john_checking.withdraw(50)  # Withdraw using overdraft
    print(f"John's checking balance: {john_checking.get_balance()}")

# Run the banking system
if __name__ == "__main__":
    banking_system()
