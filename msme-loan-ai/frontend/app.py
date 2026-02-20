import streamlit as st
import requests

st.title("MSME Loan Eligibility AI Assistant")

# Inputs from user
cibil = st.number_input("CIBIL Score")
turnover = st.number_input("Monthly Turnover")
emi = st.number_input("Existing EMI")
profit = st.number_input("Net Profit")

# Button action
if st.button("Check Eligibility"):
    response = requests.post(
        "http://127.0.0.1:8000/evaluate",
        json={
            "cibil": cibil,
            "monthly_turnover": turnover,
            "existing_emi": emi,
            "net_profit": profit
        }
    )

    result = response.json()
    st.write(result)