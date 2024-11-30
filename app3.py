import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Title and Introduction
st.title("Investment Advisor - Financial Analysis Tool")
st.write("The objective of this application is to help financial investment advisors to draw a detailed investment plan for investors. Provide detailed financial details, and the system will assist in analyzing and deriving a tailored investment strategy.")

# Module 1: Capture User's Financial Goals
st.header("Module 1: Financial Goals of the Investor")
goals = []
num_goals = st.number_input("How many financial goals does the investor have?", min_value=0, value=1)

for i in range(num_goals):
    goal_name = st.text_input(f"Goal {i+1} Name", f"Goal {i+1}")
    goal_start_year = st.number_input(f"Goal {i+1} Planning Start Year", min_value=datetime.datetime.now().year, step=1)
    cost_at_planning = st.number_input(f"Cost of Goal {i+1} in Planning Year", min_value=0.0, step=1000.0)
    goal_inflation = st.number_input(f"Goal {i+1} Expected Inflation (%)", min_value=0.0, max_value=100.0, step=0.1)
    target_year = st.number_input(f"Goal {i+1} Target Year", min_value=goal_start_year, step=1)
    sip_interest_rate = st.number_input(f"Goal {i+1} SIP Interest Rate (%)", min_value=0.0, max_value=100.0, step=0.1)
    monthly_sip = st.number_input(f"Goal {i+1} Monthly SIP to Achieve Goal", min_value=0.0, step=100.0)
    goals.append([goal_name, goal_start_year, cost_at_planning, goal_inflation, target_year, sip_interest_rate, monthly_sip])

if goals:
    goals_df = pd.DataFrame(goals, columns=["Goal Name", "Planning Start Year", "Cost (Planning Year)", "Inflation (%)", "Target Year", "SIP Interest Rate (%)", "Monthly SIP"])
    goals_df["Number of Years"] = goals_df["Target Year"] - goals_df["Planning Start Year"]
    goals_df["Cost at Target Year"] = goals_df["Cost (Planning Year)"] * ((1 + (goals_df["Inflation (%)"] / 100)) ** goals_df["Number of Years"])
    st.write("### Goals Table")
    st.write(goals_df)

# Module 2: Current Financial Portfolio
st.header("Module 2: Current Financial Portfolio")

# a. Existing Investment Portfolio
st.subheader("a. Existing Investment Portfolio")
investments = []
num_investments = st.number_input("Number of current investments", min_value=0, value=1)

for i in range(num_investments):
    investment_name = st.text_input(f"Investment {i+1} Name")
    annual_premium = st.number_input(f"Annual Premium for Investment {i+1}", min_value=0.0, step=1000.0)
    maturity_date = st.date_input(f"Maturity Date for Investment {i+1}")
    maturity_value = st.number_input(f"Maturity Value for Investment {i+1}", min_value=0.0, step=1000.0)
    last_premium_date = st.date_input(f"Last Premium Payment Date for Investment {i+1}")
    sum_assured = st.number_input(f"Sum Assured for Investment {i+1}", min_value=0.0, step=1000.0)
    cash_payout = st.number_input(f"Cash Payout for Investment {i+1}", min_value=0.0, step=1000.0)
    cash_payout_periodicity = st.selectbox(f"Periodicity of Cash Payout for Investment {i+1}", ["Monthly", "Quarterly", "Annually", "None"])
    investments.append([investment_name, annual_premium, maturity_date, maturity_value, last_premium_date, sum_assured, cash_payout, cash_payout_periodicity])

if investments:
    investments_df = pd.DataFrame(investments, columns=["Investment Name", "Annual Premium", "Maturity Date", "Maturity Value", "Last Premium Date", "Sum Assured", "Cash Payout", "Cash Payout Periodicity"])
    st.write("### Existing Investment Portfolio")
    st.write(investments_df)

# b. Existing Assets Owned
st.subheader("b. Existing Assets Owned")
assets = []
num_assets = st.number_input("Number of assets owned", min_value=0, value=1)

for i in range(num_assets):
    asset_name = st.text_input(f"Asset {i+1} Name")
    asset_value = st.number_input(f"Value of Asset {i+1}", min_value=0.0, step=1000.0)
    assets.append([asset_name, asset_value])

if assets:
    assets_df = pd.DataFrame(assets, columns=["Asset Name", "Value"])
    st.write("### Existing Assets")
    st.write(assets_df)

# c. Existing Cash Inflows
st.subheader("c. Existing Cash Inflows")
inflows = []
num_members = st.number_input("Number of family members with income", min_value=0, value=1)

for i in range(num_members):
    member_name = st.text_input(f"Family Member {i+1} Name")
    monthly_income = st.number_input(f"Monthly Income of {member_name}", min_value=0.0, step=1000.0)
    inflows.append([member_name, monthly_income])

if inflows:
    inflows_df = pd.DataFrame(inflows, columns=["Family Member Name", "Monthly Income"])
    st.write("### Existing Cash Inflows")
    st.write(inflows_df)

# Module 3: Current Insurance Portfolio
st.header("Module 3: Current Insurance Portfolio Details")
insurance = []
num_insurance = st.number_input("Number of insurance policies", min_value=0, value=1)

for i in range(num_insurance):
    policy_name = st.text_input(f"Policy {i+1} Name")
    annual_premium = st.number_input(f"Annual Premium for {policy_name}", min_value=0.0, step=1000.0)
    num_family_members_covered = st.number_input(f"Number of Family Members Covered for {policy_name}", min_value=1, step=1)
    policy_type = st.selectbox(f"Is {policy_name} Floating or Fixed?", ["Floating", "Fixed"])
    sum_assured = st.number_input(f"Sum Assured for {policy_name}", min_value=0.0, step=1000.0)
    insurance.append([policy_name, annual_premium, num_family_members_covered, policy_type, sum_assured])

if insurance:
    insurance_df = pd.DataFrame(insurance, columns=["Policy Name", "Annual Premium", "Family Members Covered", "Policy Type", "Sum Assured"])
    st.write("### Insurance Portfolio")
    st.write(insurance_df)

# Module 4: Monthly Expenses
st.header("Module 4: Monthly Expenses")
expenses = []
num_expenses = st.number_input("Number of recurring monthly expenses", min_value=0, value=1)

for i in range(num_expenses):
    expense_name = st.text_input(f"Expense {i+1} Name")
    monthly_expense = st.number_input(f"Monthly Amount for {expense_name}", min_value=0.0, step=100.0)
    expenses.append([expense_name, monthly_expense])

if expenses:
    expenses_df = pd.DataFrame(expenses, columns=["Expense Name", "Monthly Amount"])
    st.write("### Monthly Expenses")
    st.write(expenses_df)

# Summary Report
st.header("Summary Report")
st.write("Based on the provided details, the application helps in understanding the current financial state of the investor and extrapolating requirements to meet future financial goals.")

# Option to download a CSV of all the modules
data_frames = [goals_df, investments_df, assets_df, inflows_df, insurance_df, expenses_df]
all_data_df = pd.concat(data_frames, keys=["Goals", "Investments", "Assets", "Inflows", "Insurance", "Expenses"])

csv = all_data_df.to_csv().encode('utf-8')
st.download_button(
    label="Download Financial Data as CSV",
    data=csv,
    file_name='financial_data.csv',
    mime='text/csv',
)

st.button("Generate Detailed Investment Plan")
