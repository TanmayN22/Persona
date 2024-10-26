import streamlit as st
import google.generativeai as genai
import matplotlib.pyplot as plt
import time
import json
import re
import os

class Pages_switch():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/Questions.py", label="Questionnaire")
    st.sidebar.page_link("pages/DashBoard.py", label="Dashboard")
    st.sidebar.page_link("pages/news.py", label="News & Trends")
    st.sidebar.page_link("pages/educational.py", label="Educational")
    st.sidebar.page_link("pages/aboutus.py", label="About us")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
st.title("Personalized Investment Portfolio Builder")

# Create tabs for different sections of the questionnaire
tabs = st.tabs(["Personal Information", "Financial Details", "Investments", "Risk Profile", "Submit"])

# Personal Information Tab
with tabs[0]:
    st.header("Personal Information")
    age = st.selectbox("Enter your age:", list(range(12, 100)))
    income = st.text_input("Enter your income per annum:", value="0")
    monthly_expenses = st.text_input("Enter your monthly expenditure:", value="0")

# Financial Details Tab
with tabs[1]:
    st.header("Financial Details")
    savings_goal = st.text_input("Enter the total amount of money you want to save:", value="0")
    current_savings = st.text_input("Enter your current savings amount:", value="0")
    total_debts = st.text_input("Enter your total outstanding debts (e.g., loans, credit card balances):", value="0")
    monthly_debt_payments = st.text_input("Enter your monthly payments toward these debts:", value="")
    
    # Emergency Fund
    emergency_fund = st.selectbox("Do you have an emergency fund?", ['yes', 'no'])
    if emergency_fund == 'yes':
        emergency_fund_months = st.selectbox("How many months of expenses does your emergency fund cover?", list(range(1,100)))

# Investments Tab
with tabs[2]:
    st.header("Investments")
    investment_amount = st.text_input("Enter the amount already invested:", value="0")
    investment_type = st.text_input("Enter the types of investments made (e.g., stocks, bonds, crypto):", value="")
    expected_returns = st.text_input("Enter the expected return rate of your investments (e.g., 7 for 7%, NO NEED TO PUT '%'):", value="0.0")
    time_horizon = st.selectbox("Enter your investment period in years:", list(range(1, 100)))

# Risk Profile Tab
with tabs[3]:
    st.header("Risk Profile")
    risk_tolerance = st.selectbox("What is your risk tolerance?", ['low', 'medium', 'high'])
    investment_style = st.selectbox("What is your investment style?", ['conservative', 'balanced', 'aggressive'])
    investment_preferences = st.text_input("Do you prefer specific asset classes?")
    financial_goals = st.text_input("List your financial goals (e.g., retirement, buying a home, children's education):", value="")
    target_amounts = st.text_input("Enter target amounts for each financial goal, separated by commas:", value="")

# Submit Tab
with tabs[4]:
    if st.button("Submit Profile"):
        with st.spinner("Processing your profile..."):
            # Validate that all fields have been filled out
            if not all([income, monthly_expenses, savings_goal, current_savings, total_debts, monthly_debt_payments, 
                        investment_amount, investment_type, expected_returns, financial_goals, target_amounts]):
                st.error("Please fill out all fields to proceed.")
            else:
                try:
                    # Parse inputs
                    income = float(income)
                    monthly_expenses = float(monthly_expenses)
                    savings_goal = float(savings_goal)
                    current_savings = float(current_savings)
                    time_horizon = int(time_horizon)
                    age = int(age)
                    investment_amount = float(investment_amount)
                    expected_returns = float(expected_returns)
                    total_debts = float(total_debts)
                    monthly_debt_payments = float(monthly_debt_payments)

                    # Construct prompt
                    prompt = (
                        f"My annual income is {income}, with a monthly expense of {monthly_expenses}. "
                        f"My savings goal is {savings_goal}, and I currently have {current_savings} saved. "
                        f"I have already invested {investment_amount} in {investment_type}, aiming for an expected return of {expected_returns}%. "
                        f"My age is {age}, and my investment horizon is {time_horizon} years. "
                        f"My risk tolerance is {risk_tolerance}, with an investment style of {investment_style}. "
                        f"I prefer investments in {investment_preferences}. "
                        f"My financial goals include {financial_goals}, with targets of {target_amounts}. "
                        f"My total debt is {total_debts}, and I pay {monthly_debt_payments} monthly towards it. "
                    )

                    if emergency_fund == 'yes':
                        emergency_fund_months = float(emergency_fund_months)
                        prompt += f"I also have an emergency fund that covers {emergency_fund_months} months of expenses. "

                    prompt += (
                        "Please provide a breakdown of how much I should allocate to Stocks, Bonds, and Crypto, "
                        "as well as a savings and debt management strategy. "
                        "Return the output in JSON format with fields for 'Stocks', 'Bonds', 'Crypto', 'Savings Strategy', "
                        "'Debt Management', and 'Emergency Fund Allocation'."
                    )

                    # Call Gemini Flash API
                    model = genai.GenerativeModel("gemini-1.5-pro-002")
                    response = model.generate_content(prompt)
                    
                    # Access response text directly
                    ai_response = response.text  # Use the 'text' attribute directly

                    # Store response and flag for display
                    st.session_state.response = ai_response
                    st.session_state.show_results = True
                    st.success("Your profile has been successfully submitted! You can now go to the Dashboard.")
                    time.sleep(8)
                    st.rerun()

                except ValueError as ve:
                    st.error(f"Input error: {ve}")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
