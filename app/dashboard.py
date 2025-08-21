import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/HR-Employee-Attrition.csv")
df['Attrition'] = df['Attrition'].map({'Yes':1, 'No':0})

# Dashboard Title
st.title("HR Analytics - Employee Attrition Dashboard")

# KPIs
attrition_rate = df['Attrition'].mean() * 100
avg_salary = df['MonthlyIncome'].mean()
avg_age = df['Age'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Attrition Rate", f"{attrition_rate:.2f}%")
col2.metric("Avg Salary", f"${avg_salary:,.0f}")
col3.metric("Avg Age", f"{avg_age:.1f}")

# Chart 1: Attrition by Department
fig1 = px.histogram(df, x="Department", color="Attrition", barmode="group")
st.plotly_chart(fig1)

# Chart 2: Attrition by Job Role
fig2 = px.histogram(df, x="JobRole", color="Attrition", barmode="group")
st.plotly_chart(fig2)

# Chart 3: Salary vs Attrition
fig3 = px.box(df, x="Attrition", y="MonthlyIncome")
st.plotly_chart(fig3)
