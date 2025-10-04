# app.py

import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------
# Load Models
# -------------------------------
try:
    rf_model = joblib.load("random_forest_model.joblib")
    xgb_model = joblib.load("xgboost_model.joblib")
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# -------------------------------
# Prediction Page (Only)
# -------------------------------
st.title("🔮 Ola Driver Leave Prediction")

# Feature Order (must match training)
feature_cols = [
    "Total Business Value",   # ✅ consistent spelling
    "Quarterly Rating",
    "Age",
    "Tenure_Days",
    "Grade",
    "Gender",
    "Income"
]

# -----------------------
# 1️⃣ Manual Input
# -----------------------
st.subheader("Enter Driver Info Manually")

Age = st.number_input("Age", 18, 65, 30)
Tenure_Days = st.number_input("Tenure (Days)", 0, 5000, 365)
Income = st.number_input("Income", 10000, 200000, 50000)
Gender = st.selectbox("Gender", [0, 1])  # 0=Male, 1=Female
Grade = st.number_input("Grade", 0, 10, 5)
Quarterly_Rating = st.number_input("Quarterly Rating", 0, 5, 3)
Total_Business_Value = st.number_input("Total Business Value", 0, 100000, 1000)

input_data = pd.DataFrame([[
    Total_Business_Value, Quarterly_Rating, Age, Tenure_Days, Grade, Gender, Income
]], columns=feature_cols)

if st.button("Predict Manually"):
    rf_pred = rf_model.predict(input_data)[0]
    xgb_pred = xgb_model.predict(input_data)[0]

    if rf_pred == 1:
        st.error("Random Forest Prediction: Leave")
    else:
        st.success("Random Forest Prediction: Stay")

    if xgb_pred == 1:
        st.error("XGBoost Prediction: Leave")
    else:
        st.success("XGBoost Prediction: Stay")
