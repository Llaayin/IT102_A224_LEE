"""
######### Learning Signature #########
Programmed by: Aaron Jared Lee
Date Submitted: September 13, 2026

Program Description: This program saves a text e-receipt for each transaction into the receipts folder and provides functions to read receipts back.

Reflection: I learned how to write formatted receipts to disk and read them back for display in the Streamlit app.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""

# [NEW] E-Receipt module
import os
from datetime import datetime


RECEIPTS_FOLDER = "receipts"


def save_receipt(account, transaction_type, amount, extra=""):

    if not os.path.exists(RECEIPTS_FOLDER):
        os.makedirs(RECEIPTS_FOLDER)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_safe_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = (
        f"{RECEIPTS_FOLDER}/"
        f"receipt_{account.account_number}_{file_safe_time}.txt"
    )

    with open(filename, "w") as file:

        file.write("=================================\n")
        file.write("        LEE BANK RECEIPT\n")
        file.write("=================================\n")
        file.write(f"Date:           {timestamp}\n")
        file.write(f"Account Name:   {account.account_name}\n")
        file.write(f"Account No.:    {account.account_number}\n")
        file.write(f"Account Type:   {account.get_account_type()}\n")
        file.write("---------------------------------\n")
        file.write(f"Transaction:    {transaction_type}\n")
        file.write(f"Amount:         PHP {amount:.2f}\n")

        if extra:
            file.write(f"Details:        {extra}\n")

        file.write("---------------------------------\n")
        file.write(f"New Balance:    PHP {account.check_balance():.2f}\n")
        file.write("=================================\n")
        file.write("Thank you for banking with Lee Bank.\n")
        file.write("=================================\n")

    return filename


def get_latest_receipt(account_number):

    if not os.path.exists(RECEIPTS_FOLDER):
        return None

    files = [
        f for f in os.listdir(RECEIPTS_FOLDER)
        if f.startswith(f"receipt_{account_number}_")
    ]

    if not files:
        return None

    files.sort(reverse=True)

    latest = f"{RECEIPTS_FOLDER}/{files[0]}"

    with open(latest, "r") as file:
        content = file.read()

    return content


def get_all_receipts(account_number):

    if not os.path.exists(RECEIPTS_FOLDER):
        return []

    files = [
        f for f in os.listdir(RECEIPTS_FOLDER)
        if f.startswith(f"receipt_{account_number}_")
    ]

    files.sort(reverse=True)

    return files