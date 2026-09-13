class Account:
    
    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance

    def check_balance(self):
        return self_balance

    def deposit(self, amount):
       
     if amount > 0:
       self.balance += amount
            return True

        return False

    def withdraw(self, amount):

        if amount > 0 and amount <= self.balance:

            self.balance -= amount

            return True

        return False

  if __name__ == "__main__":
    account = Account("Lee", 10000.00)
    print(f"Starting balance: \u20b1{account.check_balance():,.2f}")

    result = account.withdraw(2000.00)
    print(f"Withdraw \u20b12000.00 -> {result}")
    print(f"Expected balance: \u20b1{account.check_balance():,.2f}")

    result = account.withdraw(15000.00)
    print(f"Withdraw \u20b115000.00 -> {result}")
    print(f"Balance after failed withdrawal: \u20b1{account.check_balance():,.2f}")
