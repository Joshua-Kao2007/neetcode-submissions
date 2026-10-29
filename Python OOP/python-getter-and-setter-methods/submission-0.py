class BankAccount:
    def __init__(self, balance: int):
        pass  # Add private balance
        self._balance = balance
    
    # TODO: Add getter method for balance
    def get_balance(self):
        return self._balance
    # TODO: Add setter method for balance
    def set_balance(self, balance):
        if balance < 0:
            print("Cannot set negative balance!")
        else:
            self._balance = balance

# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
