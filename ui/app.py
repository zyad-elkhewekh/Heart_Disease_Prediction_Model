import streamlit as st
import numpy as np
import joblib
# with open("final_model.pkl", "rb") as file:
#     model = pickle.load(file)

#model = joblib.load('final_model.pkl')

import os
model_path = os.path.join(os.path.dirname(__file__), 'final_model.pkl')
model = joblib.load(model_path)


st.title("Heart Disease Prediction App")
st.write("Enter patient details to predict whether they are likely to have heart disease.")

age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3],
                  format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"][x])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, value=130)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=250)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
restecg = st.selectbox("Resting ECG Results", options=[0, 1, 2],
                       format_func=lambda x: ["Normal", "ST-T Abnormality", "Left Ventricular Hypertrophy"][x])
thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0, step=0.1, value=1.0)
slope = st.selectbox("Slope of ST Segment", options=[0, 1, 2],
                     format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x])
ca = st.slider("Number of Major Vessels Colored by Fluoroscopy (ca)", 0, 3, 0)
thal = st.selectbox("Thalassemia", options=[0, 1, 2, 3],
                    format_func=lambda x: ["Unknown", "Normal", "Fixed Defect", "Reversible Defect"][x])

features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                      thalach, exang, oldpeak, slope, ca, thal]])

if st.button("Predict"):
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.error("The patient is likely to have heart disease.")
    else:
        st.success("The patient is unlikely to have heart disease.")
