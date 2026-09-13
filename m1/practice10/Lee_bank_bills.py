"""
######### Learning Signature #########
Programmed by: Aaron Jared Lee
Date Submitted: September 13, 2026

Program Description: This program handles bill payments, validating the biller name, reference number, and amount before deducting from the account and logging the transaction.

Reflection: I learned how to add a new feature module that follows the existing pattern of validation, action, logging, and returning a result.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""

import Lee_bank_storage
import Lee_bank_transactions
import Lee_bank_receipts


def pay_bill(account, biller_name, reference_number, amount):

    biller_name = biller_name.strip()
    reference_number = reference_number.strip()

    if biller_name == "":
        return False, "Please enter the biller name."

    if reference_number == "":
        return False, "Please enter a reference number."

    if amount <= 0:
        return False, "Invalid bill amount."

    if amount > account.check_balance():
        return False, "Insufficient balance."

    success = account.withdraw(amount)

    if not success:
        return False, "Bill payment failed."

    Lee_bank_storage.update_account(account)

    Lee_bank_transactions.record_transaction(
        account,
        f"Bill Payment - {biller_name} (Ref {reference_number})",
        amount
    )

    Lee_bank_receipts.save_receipt(
        account,
        "Bill Payment",
        amount,
        extra=f"Biller: {biller_name} | Reference: {reference_number}"
    )

    return True, (
        f"Bill paid successfully. "
        f"{biller_name} (Ref {reference_number}) — "
        f"₱{amount:.2f}"
    )