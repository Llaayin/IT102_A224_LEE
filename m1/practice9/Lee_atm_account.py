class Account:
    
    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance

    def check_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance = self._balance - amount
            return True
        else:
            return False


if __name__ == "__main__":
    account = Account("Juan Dela Cruz", 10000.00)
    print(f"Starting balance: ₱{account.check_balance():,.2f}")
    
    result = account.withdraw(2000.00)
    print(f"Withdraw ₱2000.00 -> {result}")
    print(f"Expected balance: ₱{account.check_balance():,.2f}")
    
    result = account.withdraw(15000.00)
    print(f"Withdraw ₱15000.00 -> {result}")

""" 
######### Learning Signature ######### 
Programmed by: Clyde Balaman
Date Submitted: September 4, 2026

Program Description: This program implements an Account class with
deposit and withdraw methods that validate transactions before
modifying the balance.

Reflection: I learned how to encapsulate data within a class and
enforce business rules inside methods.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""
