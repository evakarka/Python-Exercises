class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        """
        Initialize a new BankAccount object.
        
        :param account_number: The account's unique identifier.
        :param account_holder: The name of the account holder.
        :param balance: Initial balance of the account, default is 0.
        """
        self.account_number = account_number  # Account number (unique identifier)
        self.account_holder = account_holder  # Account holder's name
        self.balance = balance  # Initial balance of the account
    
    def deposit(self, amount):
        """
        Deposit a specified amount into the account, increasing the balance.
        
        :param amount: The amount to deposit.
        """
        if amount > 0:
            self.balance += amount  # Increase the balance by the deposit amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")  # Error message if amount is invalid
    
    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account, ensuring no overdraft.
        
        :param amount: The amount to withdraw.
        """
        if amount > 0:  # Ensure that the withdrawal amount is positive
            if amount <= self.balance:
                self.balance -= amount  # Deduct the withdrawal amount from the balance
                print(f"Withdrew ${amount}. New balance: ${self.balance}.")
            else:
                print("Error: Insufficient funds.")  # Error if insufficient funds
        else:
            print("Withdrawal amount must be positive.")  # Error if amount is invalid
    
    def display_balance(self):
        """
        Display the current balance of the account.
        """
        print(f"Account Balance: ${self.balance}")
    
    def transfer(self, target_account, amount):
        """
        Transfer money to another account if sufficient funds exist.
        
        :param target_account: The target BankAccount object to transfer money to.
        :param amount: The amount to transfer.
        """
        if amount > 0:  # Ensure the transfer amount is positive
            if amount <= self.balance:
                # Deduct from the sender account
                self.balance -= amount
                # Add to the recipient account
                target_account.balance += amount
                print(f"Transferred ${amount} to Account {target_account.account_number}.")
                print(f"Your new balance: ${self.balance}.")
                print(f"Recipient's new balance: ${target_account.balance}.")
            else:
                print("Error: Insufficient funds for transfer.")  # Error if insufficient funds
        else:
            print("Transfer amount must be positive.")  # Error if transfer amount is invalid

# Testing the BankAccount class
if __name__ == "__main__":
    # Creating two BankAccount objects with initial balance
    account1 = BankAccount(101, "Alice", 500)
    account2 = BankAccount(102, "Bob", 300)
    
    # Display initial balances of both accounts
    account1.display_balance()
    account2.display_balance()
    
    # Test deposit method (depositing money into both accounts)
    account1.deposit(200)  # Depositing $200 into Alice's account
    account2.deposit(50)   # Depositing $50 into Bob's account
    
    # Test withdraw method (withdrawing money from both accounts)
    account1.withdraw(100)  # Withdrawing $100 from Alice's account
    account2.withdraw(400)  # Trying to withdraw more than available from Bob's account (should show error)
    
    # Test transfer method (transferring money between accounts)
    account1.transfer(account2, 150)  # Transferring $150 from Alice to Bob
    account1.transfer(account2, 700)  # Trying to transfer more than available in Alice's account (should show error)
    
    # Display final balances after all operations
    account1.display_balance()
    account2.display_balance()
