import streamlit as st
import pandas as pd
from datetime import date

# Create a DataFrame to store the spending data
spending_data = pd.DataFrame({
    "Date": ["2023-05-22", "2023-05-23"],
    "Category": ["Food", "Transportation"],
    "Amount": [15.50, 10.25]
})

# Today's date
today = date.today().strftime("%Y-%m-%d")

# Sidebar section
st.sidebar.header("Add New Spending")
category = st.sidebar.selectbox("Category", ["Food", "Transportation", "Entertainment", "Others"])
amount = st.sidebar.number_input("Amount", value=0.0, step=0.01)
if st.sidebar.button("Add"):
    spending_data = spending_data.append({"Date": today, "Category": category, "Amount": amount}, ignore_index=True)
    st.sidebar.success("Spending added successfully!")

# Main section
st.title("Daily Spending Tracker")
st.write("Track and monitor your daily spendings.")

# Show the spending data
st.header("Spending Data")
st.dataframe(spending_data)

# Show spending summary
st.header("Spending Summary")
summary_data = spending_data.groupby("Category")["Amount"].sum().reset_index()
st.dataframe(summary_data)

# Show total spending
total_spending = spending_data["Amount"].sum()
st.write(f"Total Spending: ${total_spending:.2f}")
