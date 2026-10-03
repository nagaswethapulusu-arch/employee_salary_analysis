import streamlit as st
import pandas as pd

st.title("Employee Salary Analysis")

employees = ["Asha", "Ravi", "Meena", "Kiran", "Swetha", "Harsh", "Rupesh", "Akhil"]
salaries = [45000, 52000, 38000, 75000, 60000, 42000, 58000, 90000]

total = sum(salaries)
average = total / len(salaries)
highest = max(salaries)
lowest = min(salaries)
top_earner = employees[salaries.index(highest)]
lowest_earner = employees[salaries.index(lowest)]

st.header("Summary")
c1, c2 = st.columns(2)
c1.metric("Total salary", f"₹{total:,}")
c2.metric("Average salary", f"₹{average:,.2f}")
c3, c4 = st.columns(2)
c3.metric("Highest salary", f"₹{highest:,}", top_earner)
c4.metric("Lowest salary", f"₹{lowest:,}", lowest_earner)

st.header("Comparison with average")


def get_status(salary):
    if salary > average:
        return "Above average"
    elif salary < average:
        return "Below average"
    else:
        return "Equal to average"


df = pd.DataFrame({
    "Employee": employees,
    "Salary": salaries,
    "Difference from average": [round(s - average) for s in salaries],
    "Status": [get_status(s) for s in salaries],
})
st.table(df)

st.header("Salary chart")
st.bar_chart(df.set_index("Employee")["Salary"])

st.header("Statistics (Pandas describe)")
st.table(df["Salary"].describe().round(2).to_frame("Salary"))
