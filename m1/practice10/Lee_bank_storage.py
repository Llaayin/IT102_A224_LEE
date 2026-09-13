"""
######### Learning Signature #########
Programmed by: Aaron Jared Lee
Date Submitted: September 13, 2026

Program Description: This program reads and writes bank accounts to users.txt, including savings goal data, and rebuilds the correct Account subclass when loading.

Reflection: I learned how to extend a text-file format without breaking backward compatibility.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""

from Lee_bank_account import (
    SavingsAccount,
    StudentAccount,
    CheckingAccount
)


USERS_FILE = "users.txt"


def account_exists(account_number):

    try:

        with open(USERS_FILE, "r") as file:

            for line in file:

                if line.startswith("Account Number:"):

                    saved_number = (
                        line
                        .replace("Account Number:", "")
                        .strip()
                    )

                    if saved_number == account_number:

                        return True

    except FileNotFoundError:

        return False

    return False


def save_account(account):

    with open(USERS_FILE, "a") as file:

        file.write(f"Account Number: {account.account_number}\n")
        file.write(f"Account Name: {account.account_name}\n")
        file.write(f"PIN: {account.get_pin()}\n")
        file.write(f"Account Type: {account.get_account_type()}\n")
        file.write(f"Balance: {account.check_balance():.2f}\n")

        # [ADDED] Persist savings goal
        goal = account.get_savings_goal()
        file.write(f"Savings Goal Name: {goal['name']}\n")
        file.write(f"Savings Goal Target: {goal['target']:.2f}\n")
        file.write(f"Savings Goal Saved: {goal['saved']:.2f}\n")

        file.write("\n")


def load_accounts():

    accounts = []

    try:

        with open(USERS_FILE, "r") as file:

            lines = file.readlines()

    except FileNotFoundError:

        return accounts

    current = {}

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("Account Number:"):

            current["account_number"] = (
                line.replace("Account Number:", "").strip()
            )

        elif line.startswith("Account Name:"):

            current["account_name"] = (
                line.replace("Account Name:", "").strip()
            )

        elif line.startswith("PIN:"):

            current["pin"] = (
                line.replace("PIN:", "").strip()
            )

        elif line.startswith("Account Type:"):

            current["account_type"] = (
                line.replace("Account Type:", "").strip()
            )

        elif line.startswith("Balance:"):

            current["balance"] = float(
                line.replace("Balance:", "").strip()
            )

        # [ADDED] Load savings goal fields
        elif line.startswith("Savings Goal Name:"):

            current["goal_name"] = (
                line.replace("Savings Goal Name:", "").strip()
            )

        elif line.startswith("Savings Goal Target:"):

            current["goal_target"] = float(
                line.replace("Savings Goal Target:", "").strip()
            )

        elif line.startswith("Savings Goal Saved:"):

            current["goal_saved"] = float(
                line.replace("Savings Goal Saved:", "").strip()
            )

            if (
                "account_number" in current
                and "account_name" in current
                and "pin" in current
                and "account_type" in current
                and "balance" in current
            ):

                if current["account_type"] == "Savings Account":
                    account = SavingsAccount(
                        current["account_number"],
                        current["account_name"],
                        current["pin"],
                        current["balance"]
                    )
                elif current["account_type"] == "Student Account":
                    account = StudentAccount(
                        current["account_number"],
                        current["account_name"],
                        current["pin"],
                        current["balance"]
                    )
                else:
                    account = CheckingAccount(
                        current["account_number"],
                        current["account_name"],
                        current["pin"],
                        current["balance"]
                    )

                if "goal_name" in current:
                    account._savings_goal_name = current["goal_name"]
                if "goal_target" in current:
                    account._savings_goal_target = current["goal_target"]
                if "goal_saved" in current:
                    account._savings_goal_saved = current["goal_saved"]

                accounts.append(account)

            current = {}

    return accounts


def find_account(account_number):

    accounts = load_accounts()

    for account in accounts:

        if account.account_number == account_number:

            return account

    return None


def update_account(account):

    accounts = load_accounts()

    with open(USERS_FILE, "w") as file:

        for saved_account in accounts:

            if saved_account.account_number == account.account_number:

                saved_account._balance = account.check_balance()
                saved_account._pin = account.get_pin()

                goal = account.get_savings_goal()
                saved_account._savings_goal_name = goal["name"]
                saved_account._savings_goal_target = goal["target"]
                saved_account._savings_goal_saved = goal["saved"]

            file.write(f"Account Number: {saved_account.account_number}\n")
            file.write(f"Account Name: {saved_account.account_name}\n")
            file.write(f"PIN: {saved_account.get_pin()}\n")
            file.write(f"Account Type: {saved_account.get_account_type()}\n")
            file.write(f"Balance: {saved_account.check_balance():.2f}\n")

            g = saved_account.get_savings_goal()
            file.write(f"Savings Goal Name: {g['name']}\n")
            file.write(f"Savings Goal Target: {g['target']:.2f}\n")
            file.write(f"Savings Goal Saved: {g['saved']:.2f}\n")

            file.write("\n")