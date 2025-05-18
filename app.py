import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Title
st.title("🛍️ Customer Segment Prediction using KNN")
st.markdown("Predict if a customer is **Low**, **Medium**, or **High** value based on their profile.")

# User Inputs
gender = st.selectbox("Gender", ["Female", "Male"])
age = st.slider("Age", 18, 70, 30)
annual_income = st.slider("Annual Income (in thousands)", 10, 150, 60)
spending_score = st.slider("Spending Score (1–100)", 1, 100, 50)

# Convert gender to number
gender_num = 1 if gender == "Male" else 0

# Predict Button
if st.button("Predict Segment"):
    input_data = np.array([[gender_num, age, annual_income, spending_score]])
    input_scaled = scaler.transform(input_data)
    segment = model.predict(input_scaled)[0]

    segment_labels = {0: "Low-Value Customer", 1: "Medium-Value Customer", 2: "High-Value Customer"}
    st.success(f"🧠 Predicted Segment: **{segment_labels[segment]}**")
