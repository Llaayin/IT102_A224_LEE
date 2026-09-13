"""
######### Learning Signature #########
Programmed by: Aaron Jared Lee
Date Submitted: September 13, 2026

Program Description: This program defines the BankAccount abstract base class with savings pocket support, along with SavingsAccount, StudentAccount, and CheckingAccount subclasses.

Reflection: I learned how to extend a class with new attributes and methods while keeping the original encapsulation and inheritance structure intact.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""

from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(
        self,
        account_number,
        name,
        pin,
        starting_balance
    ):
        self.account_number = account_number
        self.account_name = name

        # Encapsulation
        self._pin = pin
        self._balance = starting_balance

        # [ADDED] Savings goal (pocket) fields
        self._savings_goal_name = ""
        self._savings_goal_target = 0.0
        self._savings_goal_saved = 0.0

    # Encapsulation
    def check_balance(self):
        return self._balance

    def deposit(self, amount):

        if amount <= 0:
            return False

        self._balance += amount

        return True

    def withdraw(self, amount):

        if amount <= 0:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount

        return True

    def verify_pin(self, pin):

        return self._pin == pin

    def get_pin(self):

        return self._pin

    # [ADDED] Change PIN support
    def change_pin(self, old_pin, new_pin):

        if not self.verify_pin(old_pin):
            return False

        if not new_pin.isdigit() or len(new_pin) != 4:
            return False

        self._pin = new_pin

        return True

    # [ADDED] Savings Goal — set name + target
    def set_savings_goal(self, name, target):

        if target <= 0:
            return False

        self._savings_goal_name = name
        self._savings_goal_target = target
        self._savings_goal_saved = 0.0

        return True

    # [ADDED] Savings Goal — deposit into the pocket
    def add_to_savings_goal(self, amount):

        if amount <= 0:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount
        self._savings_goal_saved += amount

        return True

    # [ADDED] Savings Goal — read current progress
    def get_savings_goal(self):

        return {
            "name": self._savings_goal_name,
            "target": self._savings_goal_target,
            "saved": self._savings_goal_saved,
            "remaining": max(
                0.0,
                self._savings_goal_target - self._savings_goal_saved
            )
        }

    # [ADDED] Savings Goal — has one been set?
    def has_savings_goal(self):

        return self._savings_goal_target > 0

    # Abstraction
    @abstractmethod
    def get_account_type(self):
        pass


# Inheritance
class SavingsAccount(BankAccount):

    # Polymorphism
    def get_account_type(self):

        return "Savings Account"


# Inheritance
class StudentAccount(BankAccount):

    # Polymorphism
    def get_account_type(self):

        return "Student Account"


# Inheritance
class CheckingAccount(BankAccount):

    # Polymorphism
    def get_account_type(self):

        return "Checking Account"