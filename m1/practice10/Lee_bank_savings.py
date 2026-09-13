"""
######### Learning Signature #########
Programmed by: Aaron Jared Lee
Date Submitted: September 13, 2026

Program Description: This program manages savings goals, allowing users to set a custom goal, deposit toward it, and track progress.

Reflection: I learned how to build a feature that manages its own state while keeping it tied to the existing Account object.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""

# [NEW] Savings Goal module
import Lee_bank_storage
import Lee_bank_transactions
import Lee_bank_receipts


def create_goal(account, name, target):

    name = name.strip()

    if name == "":
        return False, "Please enter a goal name."

    if target <= 0:
        return False, "Goal amount must be greater than zero."

    success = account.set_savings_goal(name, target)

    if not success:
        return False, "Could not create the goal."

    Lee_bank_storage.update_account(account)

    return True, (
        f"Savings goal '{name}' set with target "
        f"₱{target:.2f}."
    )


def deposit_to_goal(account, amount):

    if amount <= 0:
        return False, "Invalid deposit amount."

    if not account.has_savings_goal():
        return False, "No active savings goal."

    if amount > account.check_balance():
        return False, "Insufficient balance."

    goal = account.get_savings_goal()

    remaining = goal["remaining"]

    if amount > remaining:
        amount = remaining

    success = account.add_to_savings_goal(amount)

    if not success:
        return False, "Could not deposit to the goal."

    Lee_bank_storage.update_account(account)

    Lee_bank_transactions.record_transaction(
        account,
        f"Savings Goal Deposit - {goal['name']}",
        amount
    )

    Lee_bank_receipts.save_receipt(
        account,
        "Savings Goal Deposit",
        amount,
        extra=f"Goal: {goal['name']}"
    )

    updated = account.get_savings_goal()

    if updated["remaining"] <= 0:
        return True, (
            f"Goal '{updated['name']}' reached! "
            f"Total saved: ₱{updated['saved']:.2f}"
        )

    return True, (
        f"₱{amount:.2f} added to '{updated['name']}'. "
        f"₱{updated['remaining']:.2f} left to reach the goal."
    )