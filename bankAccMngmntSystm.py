# Base Account class
class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        # Initialize the account with an account number, holder's name, and starting balance
        self._account_number = account_number   # Protected attribute for account number
        self._account_holder = account_holder   # Protected attribute for account holder's name
        self._balance = balance                 # Protected attribute for account balance

    def deposit(self, amount):
        # Method to deposit money into the account
        if amount > 0:
            self._balance += amount  # Add the deposit amount to the balance
        else:
            raise ValueError("Deposit amount must be positive")  # Raise error if deposit amount is not positive

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if amount > self._balance:
            raise ValueError("Insufficient funds")  # Raise error if withdrawal amount exceeds balance
        if amount > 0:
            self._balance -= amount  # Subtract the withdrawal amount from the balance
        else:
            raise ValueError("Withdrawal amount must be positive")  # Raise error if withdrawal amount is not positive

    def get_balance(self):
        # Method to return the current balance of the account
        return self._balance

    def get_account_info(self):
        # Method to return a formatted string with account details
        return f"Account Number: {self._account_number}, Holder: {self._account_holder}, Balance: {self._balance:.2f}"

# SavingsAccount class inheriting from Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        # Initialize the savings account with an interest rate
        super().__init__(account_number, account_holder, balance)  # Call the parent class constructor
        self._interest_rate = interest_rate  # Protected attribute for interest rate

    def apply_interest(self):
        # Method to apply interest to the balance
        self._balance += self._balance * self._interest_rate  # Increase balance by interest rate

    def get_account_info(self):
        # Override to include interest rate in the account details
        return f"{super().get_account_info()}, Interest Rate: {self._interest_rate:.2%}"

# CheckingAccount class inheriting from Account
class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500.0):
        # Initialize the checking account with an overdraft limit
        super().__init__(account_number, account_holder, balance)  # Call the parent class constructor
        self._overdraft_limit = overdraft_limit  # Protected attribute for overdraft limit

    def withdraw(self, amount):
        # Override the withdraw method to allow overdrafts within the limit
        if amount > self._balance + self._overdraft_limit:
            raise ValueError("Overdraft limit exceeded")  # Raise error if withdrawal exceeds overdraft limit
        if amount > 0:
            self._balance -= amount  # Subtract the withdrawal amount from the balance
        else:
            raise ValueError("Withdrawal amount must be positive")  # Raise error if withdrawal amount is not positive

    def get_account_info(self):
        # Override to include overdraft limit in the account details
        return f"{super().get_account_info()}, Overdraft Limit: {self._overdraft_limit:.2f}"

# Function to display the main menu
def display_menu():
    print("\n===== Bank Account Management System =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View Account Details")
    print("6. Exit")
    print("==========================================")

# Function to create a new account
def create_account(accounts):
    account_type = input("Enter account type (Savings/Checking): ").strip().lower()  # Get account type from user
    account_number = input("Enter account number: ")  # Get account number from user
    account_holder = input("Enter account holder name: ")  # Get account holder's name from user
    
    # Create a SavingsAccount if the user chooses "savings"
    if account_type == 'savings':
        interest_rate = float(input("Enter interest rate (e.g., 0.03 for 3%): "))  # Get interest rate
        account = SavingsAccount(account_number, account_holder, interest_rate=interest_rate)
    
    # Create a CheckingAccount if the user chooses "checking"
    elif account_type == 'checking':
        overdraft_limit = float(input("Enter overdraft limit: "))  # Get overdraft limit
        account = CheckingAccount(account_number, account_holder, overdraft_limit=overdraft_limit)
    
    # Handle invalid account type
    else:
        print("Invalid account type. Please choose either 'Savings' or 'Checking'.")
        return  # Exit the function if account type is invalid
    
    accounts[account_number] = account  # Store the new account in the accounts dictionary
    print(f"Account created successfully for {account_holder}!")

# Function to deposit money into an account
def deposit_money(accounts):
    account_number = input("Enter account number: ")  # Get account number from user
    if account_number in accounts:
        amount = float(input("Enter amount to deposit: "))  # Get deposit amount from user
        accounts[account_number].deposit(amount)  # Deposit the amount into the account
        print(f"Deposited {amount:.2f} to account {account_number}")
    else:
        print("Account not found!")  # Display error if account number is not found

# Function to withdraw money from an account
def withdraw_money(accounts):
    account_number = input("Enter account number: ")  # Get account number from user
    if account_number in accounts:
        amount = float(input("Enter amount to withdraw: "))  # Get withdrawal amount from user
        try:
            accounts[account_number].withdraw(amount)  # Withdraw the amount from the account
            print(f"Withdrew {amount:.2f} from account {account_number}")
        except ValueError as e:
            print(e)  # Display error if withdrawal is not possible
    else:
        print("Account not found!")  # Display error if account number is not found

# Function to check the balance of an account
def check_balance(accounts):
    account_number = input("Enter account number: ")  # Get account number from user
    if account_number in accounts:
        balance = accounts[account_number].get_balance()  # Retrieve the balance of the account
        print(f"Balance for account {account_number} is {balance:.2f}")
    else:
        print("Account not found!")  # Display error if account number is not found

# Function to view details of an account
def view_account_details(accounts):
    account_number = input("Enter account number: ")  # Get account number from user
    if account_number in accounts:
        print(accounts[account_number].get_account_info())  # Display the account details
    else:
        print("Account not found!")  # Display error if account number is not found

# Main function to run the program
def main():
    accounts = {}  # Dictionary to store all accounts
    while True:
        display_menu()  # Show the menu to the user
        choice = input("Enter your choice (1-6): ").strip()  # Get user's choice
        
        if choice == '1':
            create_account(accounts)  # Call function to create a new account
        elif choice == '2':
            deposit_money(accounts)  # Call function to deposit money into an account
        elif choice == '3':
            withdraw_money(accounts)  # Call function to withdraw money from an account
        elif choice == '4':
            check_balance(accounts)  # Call function to check balance of an account
        elif choice == '5':
            view_account_details(accounts)  # Call function to view account details
        elif choice == '6':
            print("Exiting the program. Goodbye!")  # Exit the program
            break
        else:
            print("Invalid choice. Please select a valid option.")  # Display error for invalid menu choice

# Entry point of the program
if __name__ == "__main__":
    main()  # Start the main function
