# Define the base Account class
class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        # Initialize the account with number, holder, and balance
        self._account_number = account_number  # Protected attribute for the account number
        self._account_holder = account_holder  # Protected attribute for the account holder's name
        self._balance = balance                # Protected attribute for the account balance

    def deposit(self, amount):
        # Deposit a certain amount to the account
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        # Withdraw a certain amount from the account, if sufficient balance
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive")

    def get_balance(self):
        # Return the current balance
        return self._balance

    def get_account_info(self):
        # Return a formatted string with account details
        return f"Account Number: {self._account_number}, Account Holder: {self._account_holder}, Balance: {self._balance:.2f}"

    def save_to_file(self, filename):
        # Save account details to a file
        with open(filename, 'a') as file:
            file.write(f"{self._account_number},{self._account_holder},{self._balance}\n")

# Define the SavingsAccount class inheriting from Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        # Initialize the savings account with interest rate
        super().__init__(account_number, account_holder, balance)  # Call the parent constructor
        self._interest_rate = interest_rate  # Protected attribute for the interest rate

    def apply_interest(self):
        # Apply interest to the balance
        self._balance += self._balance * self._interest_rate

    def get_account_info(self):
        # Override to include interest rate in account details
        return f"{super().get_account_info()}, Interest Rate: {self._interest_rate:.2%}"

# Define the CheckingAccount class inheriting from Account
class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500.0):
        # Initialize the checking account with overdraft limit
        super().__init__(account_number, account_holder, balance)  # Call the parent constructor
        self._overdraft_limit = overdraft_limit  # Protected attribute for the overdraft limit

    def withdraw(self, amount):
        # Allow withdrawal even if it exceeds balance, but not overdraft limit
        if amount > self._balance + self._overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive")

    def get_account_info(self):
        # Override to include overdraft limit in account details
        return f"{super().get_account_info()}, Overdraft Limit: {self._overdraft_limit:.2f}"

# Example usage
if __name__ == "__main__":
    # Create instances of SavingsAccount and CheckingAccount
    savings = SavingsAccount("SA12345", "Alice", 1000.0, 0.03)
    checking = CheckingAccount("CA54321", "Bob", 500.0, 300.0)

    # Perform operations
    savings.deposit(200)
    savings.apply_interest()
    checking.withdraw(600)

    # Save account details to a file
    savings.save_to_file("accounts.txt")
    checking.save_to_file("accounts.txt")

    # Print account information
    print(savings.get_account_info())  # Output: Account info with interest rate
    print(checking.get_account_info()) # Output: Account info with overdraft limit
