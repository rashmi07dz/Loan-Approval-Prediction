import streamlit as st
import pandas as pd
import pickle as pk

# Load models
model = pk.load(open('model.pkl', 'rb'))
scaler = pk.load(open('scaler.pkl', 'rb'))
label_encoder = pk.load(open('target_label_encoder.pkl', 'rb'))

st.header('🏦 Loan Prediction App')

# User input
gender = st.selectbox('Gender', ['Male', 'Female'])
married = st.selectbox('Marital Status', ['Yes', 'No'])
dependents = st.slider('Number of Dependents', 0, 3, 0)
education = st.selectbox('Education Level', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
applicant_income = st.number_input('Applicant Income', min_value=0, value=5000)
coapplicant_income = st.number_input('Coapplicant Income', min_value=0, value=1000)
loan_amount = st.number_input('Loan Amount (in thousands)', min_value=0, value=100)
loan_amount_term = st.selectbox('Loan Amount Term (months)', [360, 180, 480, 300, 84, 120, 240, 60, 36, 12])
credit_history = st.selectbox('Credit History', [1.0, 0.0])
property_area = st.selectbox('Property Area', ['Urban', 'Rural', 'Semiurban'])

# Encode categorical variables
gender = 1 if gender == 'Male' else 0
married = 1 if married == 'Yes' else 0
education = 1 if education == 'Graduate' else 0
self_employed = 1 if self_employed == 'Yes' else 0
property_area = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}[property_area]

# Compute Income_Per_Loan feature
income_per_loan = applicant_income / loan_amount if loan_amount > 0 else 0  # ✅ Extra feature added

# Create input DataFrame with all required features
input_data = pd.DataFrame({
    'Gender': [gender],
    'Married': [married],
    'Dependents': [dependents],
    'Education': [education],
    'Self_Employed': [self_employed],
    'ApplicantIncome': [applicant_income],
    'CoapplicantIncome': [coapplicant_income],
    'LoanAmount': [loan_amount],
    'Loan_Amount_Term': [loan_amount_term],
    'Credit_History': [credit_history],
    'Property_Area': [property_area],
})

# Scale numerical features
try:
    scaled_input = scaler.transform(input_data)
except ValueError as e:
    st.error(f"Feature mismatch error: {e}")
    st.stop()

# Make prediction
prediction = model.predict(scaled_input)

# Convert prediction to readable format
predicted_label = label_encoder.inverse_transform(prediction)[0]

# Display result
if st.button('🔍 Predict Loan Approval'):
    if predicted_label == 'Y':
        st.success('✅ Loan Approved')
    else:
        st.error('❌ Loan Not Approved')
