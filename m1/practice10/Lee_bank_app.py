"""
######### Learning Signature #########
Programmed by: Aaron Jared Lee
Date Submitted: September 13, 2026

Program Description: This is the main Streamlit interface of the Lee Bank application, providing login, registration, dashboard, deposit, withdrawal, bill payment, savings goal, e-receipts, transaction history, and analysis with a dark red and gold banking theme.

Reflection: I learned how to extend a modular Streamlit app with new features while keeping the existing OOP structure and UI theme intact.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[x] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""

import streamlit as st

import Lee_bank_auth
import Lee_bank_storage
import Lee_bank_transactions
import Lee_bank_analysis
import Lee_bank_utils
import Lee_bank_bills         # [ADDED]
import Lee_bank_savings       # [ADDED]
import Lee_bank_receipts      # [ADDED]


st.set_page_config(
    page_title="Lee Bank",
    page_icon="🏦",
    layout="wide"
)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:wght@400;600;700&display=swap');

    .stApp {
        background-color: #5a0e0e !important;
        font-family: 'Lora', serif !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #d4af37 !important;
        font-family: 'Lora', serif !important;
    }

    label {
        color: #d4af37 !important;
        font-family: 'Lora', serif !important;
    }

    .stMarkdown, .stCaption, .stText {
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #7a1515 !important;
    }

    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] .stCaption,
    section[data-testid="stSidebar"] p {
        color: #ffffff !important;
    }

    div.stButton > button {
        background-color: #d4af37 !important;
        color: #5a0e0e !important;
        border: 1px solid #b8860b !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
    }

    div.stButton > button:hover {
        background-color: #b8860b !important;
        color: #ffffff !important;
    }

    div[data-testid="stMetricValue"] {
        color: #d4af37 !important;
        font-weight: 700 !important;
    }

    div[data-testid="stMetricLabel"] {
        color: #ffffff !important;
    }

    div[data-baseweb="input"] input,
    div[data-baseweb="textarea"] textarea {
        background-color: #7a1515 !important;
        color: #ffffff !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #7a1515 !important;
        color: #ffffff !important;
    }

    div[data-baseweb="tab-list"] button {
        color: #ffffff !important;
    }

    div[data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #d4af37 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "account" not in st.session_state:
    st.session_state.account = None


st.title("🏦 LEE BANK")
st.caption("✨ Secure Digital Banking System")
st.divider()


if not st.session_state.logged_in:

    login_tab, register_tab = st.tabs(["🔑 Login", "📝 Register"])

    with login_tab:

        st.subheader("👋 Welcome Back")

        account_number = st.text_input("🔢 Account Number", key="login_account")
        pin = st.text_input("🔐 PIN", type="password", key="login_pin")

        if st.button("🔓 Login", use_container_width=True):

            account, message = Lee_bank_auth.login_account(
                account_number,
                pin
            )

            if account is not None:
                st.session_state.logged_in = True
                st.session_state.account = account
                st.success(f"✅ {message}")
                st.rerun()
            else:
                st.error(f"❌ {message}")

    with register_tab:

        st.subheader("📝 Create Your Lee Bank Account")

        name = st.text_input("👤 Full Name", key="register_name")
        account_number = st.text_input("🔢 Account Number", key="register_account")
        pin = st.text_input("🔐 Create 4-Digit PIN", type="password", key="register_pin")
        confirm_pin = st.text_input("🔐 Confirm PIN", type="password", key="register_confirm_pin")

        account_type = st.selectbox(
            "📋 Account Type",
            ["Savings Account", "Student Account", "Checking Account"]
        )

        starting_balance = st.number_input(
            "💰 Starting Balance",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )

        if st.button("✨ Create Account", use_container_width=True):

            account, message = Lee_bank_auth.register_account(
                name,
                account_number,
                pin,
                confirm_pin,
                account_type,
                starting_balance
            )

            if account is not None:
                st.success(f"✅ {message}")
                st.info("ℹ️ Your account has been created. Please use the Login tab.")
            else:
                st.error(f"❌ {message}")


else:

    account = st.session_state.account

    st.sidebar.title("🏦 LEE BANK")
    st.sidebar.caption("✨ Digital Banking Portal")
    st.sidebar.write(f"👤 **{account.account_name}**")
    st.sidebar.caption(f"📋 {account.get_account_type()}")
    st.sidebar.caption(f"🔢 Account: {account.account_number}")
    st.sidebar.divider()

    # [CHANGED] added three new menu options
    menu = st.sidebar.radio(
        "💼 BANKING MENU",
        [
            "🏠 Dashboard",
            "💵 Deposit",
            "💸 Withdraw",
            "🧾 Pay Bill",
            "🎯 Savings Goal",
            "📄 E-Receipt",
            "📜 Transaction History",
            "📊 Transaction Analysis"
        ]
    )

    st.sidebar.divider()

    if st.sidebar.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.account = None
        st.rerun()


    if menu == "🏠 Dashboard":

        st.header(f"👋 Welcome, {account.account_name}")
        st.subheader("📊 Account Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "💰 Current Balance",
            Lee_bank_utils.format_currency(account.check_balance())
        )
        col2.metric(
            "📋 Account Type",
            account.get_account_type()
        )
        col3.metric(
            "🔢 Account Number",
            account.account_number
        )

        # [ADDED] savings goal summary on the dashboard
        if account.has_savings_goal():

            goal = account.get_savings_goal()

            st.divider()
            st.subheader(f"🎯 Savings Goal: {goal['name']}")

            g1, g2, g3 = st.columns(3)
            g1.metric(
                "Saved",
                Lee_bank_utils.format_currency(goal["saved"])
            )
            g2.metric(
                "Target",
                Lee_bank_utils.format_currency(goal["target"])
            )
            g3.metric(
                "Remaining",
                Lee_bank_utils.format_currency(goal["remaining"])
            )

            if goal["target"] > 0:
                progress = min(1.0, goal["saved"] / goal["target"])
                st.progress(progress)
                st.caption(f"{progress * 100:.1f}% of the goal reached")

        st.divider()
        st.info("ℹ️ Select a banking service from the menu on the left.")


    elif menu == "💵 Deposit":

        st.header("💵 Deposit Money")
        st.write(
            f"💰 Current Balance: "
            f"**{Lee_bank_utils.format_currency(account.check_balance())}**"
        )

        amount = st.number_input(
            "💵 Deposit Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )

        if st.button("✅ Confirm Deposit", use_container_width=True):

            if not Lee_bank_utils.is_valid_amount(amount):
                st.error("❌ Invalid deposit amount.")
            else:
                success = account.deposit(amount)

                if success:
                    Lee_bank_storage.update_account(account)
                    Lee_bank_transactions.record_transaction(account, "Deposit", amount)
                    st.success("✅ Deposit successful.")
                    st.metric(
                        "💰 New Balance",
                        Lee_bank_utils.format_currency(account.check_balance())
                    )


    elif menu == "💸 Withdraw":

        st.header("💸 Withdraw Money")
        st.write(
            f"💰 Available Balance: "
            f"**{Lee_bank_utils.format_currency(account.check_balance())}**"
        )

        amount = st.number_input(
            "💸 Withdrawal Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )

        if st.button("✅ Confirm Withdrawal", use_container_width=True):

            if not Lee_bank_utils.is_valid_amount(amount):
                st.error("❌ Invalid withdrawal amount.")
            elif amount > account.check_balance():
                st.error("❌ Insufficient balance.")
            else:
                success = account.withdraw(amount)

                if success:
                    Lee_bank_storage.update_account(account)
                    Lee_bank_transactions.record_transaction(account, "Withdraw", amount)
                    st.success("✅ Withdrawal successful.")
                    st.metric(
                        "💰 New Balance",
                        Lee_bank_utils.format_currency(account.check_balance())
                    )


    # [ADDED] Bills Payment
    elif menu == "🧾 Pay Bill":

        st.header("🧾 Pay Bill")

        biller_name = st.text_input(
            "🏢 Biller Name",
            key="bill_biller",
            placeholder="e.g. Meralco, Maynilad, PLDT"
        )

        reference_number = st.text_input(
            "🔢 Reference Number",
            key="bill_ref",
            placeholder="e.g. 12345678"
        )

        amount = st.number_input(
            "💵 Bill Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f",
            key="bill_amount"
        )

        if st.button("✅ Confirm Payment", use_container_width=True):

            success, message = Lee_bank_bills.pay_bill(
                account,
                biller_name,
                reference_number,
                amount
            )

            if success:
                st.success(f"✅ {message}")
                st.metric(
                    "💰 New Balance",
                    Lee_bank_utils.format_currency(account.check_balance())
                )
            else:
                st.error(f"❌ {message}")


    # [ADDED] Savings Goal
    elif menu == "🎯 Savings Goal":

        st.header("🎯 Savings Goal")

        if not account.has_savings_goal():

            st.subheader("Set a New Goal")

            goal_name = st.text_input(
                "🎯 Goal Name",
                key="goal_name_input",
                placeholder="e.g. New Laptop, Emergency Fund"
            )

            goal_target = st.number_input(
                "💵 Target Amount",
                min_value=0.0,
                step=500.0,
                format="%.2f",
                key="goal_target_input"
            )

            if st.button("✨ Create Goal", use_container_width=True):

                success, message = Lee_bank_savings.create_goal(
                    account,
                    goal_name,
                    goal_target
                )

                if success:
                    st.success(f"✅ {message}")
                    st.rerun()
                else:
                    st.error(f"❌ {message}")

        else:

            goal = account.get_savings_goal()

            st.subheader(f"🎯 Goal: {goal['name']}")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "💰 Saved",
                Lee_bank_utils.format_currency(goal["saved"])
            )
            col2.metric(
                "🎯 Target",
                Lee_bank_utils.format_currency(goal["target"])
            )
            col3.metric(
                "📉 Remaining",
                Lee_bank_utils.format_currency(goal["remaining"])
            )

            if goal["target"] > 0:
                progress = min(1.0, goal["saved"] / goal["target"])
                st.progress(progress)
                st.caption(
                    f"{progress * 100:.1f}% of the goal reached — "
                    f"₱{goal['remaining']:.2f} left to go"
                )

            if goal["remaining"] <= 0:

                st.success("🎉 Goal reached! Great job.")

            else:

                st.subheader("💵 Deposit to this Goal")

                deposit_amount = st.number_input(
                    "Amount to Add",
                    min_value=0.0,
                    step=100.0,
                    format="%.2f",
                    key="goal_deposit_amount"
                )

                if st.button("✅ Add to Goal", use_container_width=True):

                    success, message = (
                        Lee_bank_savings.deposit_to_goal(
                            account,
                            deposit_amount
                        )
                    )

                    if success:
                        st.success(f"✅ {message}")
                        st.rerun()
                    else:
                        st.error(f"❌ {message}")


    # [ADDED] E-Receipt
    elif menu == "📄 E-Receipt":

        st.header("📄 E-Receipt")

        receipt = Lee_bank_receipts.get_latest_receipt(
            account.account_number
        )

        if receipt is None:

            st.info("ℹ️ No receipts yet. Make a transaction first.")

        else:

            st.subheader("Latest Receipt")

            st.code(receipt, language="text")

            all_receipts = Lee_bank_receipts.get_all_receipts(
                account.account_number
            )

            st.caption(
                f"📁 You have {len(all_receipts)} saved receipts "
                f"in the receipts/ folder."
            )


    elif menu == "📜 Transaction History":

        st.header("📜 Transaction History")

        transactions = Lee_bank_transactions.get_transactions()
        transactions = [
            t for t in transactions
            if t.get("account_number") == account.account_number
        ]

        if transactions:

            display_data = []
            for t in transactions:
                display_data.append({
                    "🕒 Timestamp": t.get("timestamp", "N/A"),
                    "💼 Transaction": t.get("transaction", "N/A"),
                    "💵 Amount": Lee_bank_utils.format_currency(t.get("amount", 0)),
                    "💰 Balance After": Lee_bank_utils.format_currency(t.get("balance_after", 0))
                })

            st.dataframe(display_data, use_container_width=True, hide_index=True)

        else:
            st.info("ℹ️ No transaction history available.")


    elif menu == "📊 Transaction Analysis":

        st.header("📊 Transaction Analysis")

        result = Lee_bank_analysis.analyze_transactions(account.account_number)

        st.subheader("1️⃣ Transaction Summary")
        col1, col2, col3 = st.columns(3)
        col1.metric("🧾 Total Transactions", result["total_transactions"])
        col2.metric("💵 Deposits", result["deposits"])
        col3.metric("💸 Withdrawals", result["withdrawals"])

        st.divider()

        st.subheader("2️⃣ Money Flow Analysis")
        col1, col2, col3 = st.columns(3)
        col1.metric("📥 Total Deposited", Lee_bank_utils.format_currency(result["total_deposited"]))
        col2.metric("📤 Total Withdrawn", Lee_bank_utils.format_currency(result["total_withdrawn"]))
        col3.metric("💹 Net Cash Flow", Lee_bank_utils.format_currency(result["net_cash_flow"]))

        st.divider()

        st.subheader("3️⃣ Account Activity Analysis")
        col1, col2, col3 = st.columns(3)
        col1.metric("🏆 Largest Transaction", Lee_bank_utils.format_currency(result["largest_transaction"]))
        col2.metric("📊 Average Transaction", Lee_bank_utils.format_currency(result["average_transaction"]))
        col3.metric("🕒 Latest Transaction", result["latest_transaction"])

        st.caption(f"🕒 Latest Activity: {result['latest_timestamp']}")