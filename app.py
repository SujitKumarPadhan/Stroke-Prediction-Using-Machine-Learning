import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("stroke_prediction_model.pkl")

st.set_page_config(page_title="Stroke Prediction", page_icon="❤️")

st.title("❤️ Stroke Prediction App")

st.write("Enter Patient Details")

gender = st.selectbox("Gender", ["Male", "Female", "Other"])

age = st.number_input(
    "Age",
    min_value=0,
    max_value=120,
    value=45
)

hypertension = st.selectbox(
    "Hypertension",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

heart_disease = st.selectbox(
    "Heart Disease",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

ever_married = st.selectbox(
    "Ever Married",
    ["Yes", "No"]
)

work_type = st.selectbox(
    "Work Type",
    ["Private", "Self-employed", "Govt_job", "children", "Never_worked"]
)

Residence_type = st.selectbox(
    "Residence Type",
    ["Urban", "Rural"]
)

avg_glucose_level = st.number_input(
    "Average Glucose Level",
    value=100.0
)

bmi = st.number_input(
    "BMI",
    value=25.0
)

smoking_status = st.selectbox(
    "Smoking Status",
    ["formerly smoked", "never smoked", "smokes", "Unknown"]
)

if st.button("Predict"):

    data = pd.DataFrame({

        "gender":[gender],
        "age":[age],
        "hypertension":[hypertension],
        "heart_disease":[heart_disease],
        "ever_married":[ever_married],
        "work_type":[work_type],
        "Residence_type":[Residence_type],
        "avg_glucose_level":[avg_glucose_level],
        "bmi":[bmi],
        "smoking_status":[smoking_status]

    })

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0]

    if prediction == 1:
        st.error("⚠ High Stroke Risk")
    else:
        st.success("✅ Low Stroke Risk")

    
