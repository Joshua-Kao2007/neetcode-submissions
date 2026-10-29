class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 2
    total_balance = 3000
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance


# TODO: Create two accounts
# TODO: Print the information using the mentioned format
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 2000)
print(f"Alice's balance: ${alice.balance}")
print(f"Bob's balance: ${bob.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")

