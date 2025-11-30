class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional starting balance."""
        self._balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw money if sufficient balance exists."""
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current balance: ${self._balance:.2f}")
