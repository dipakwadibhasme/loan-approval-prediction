import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.set_page_config(page_title='Loan Approval Predictor',layout="centered")
st.title("🏦 Loan Approval Prediction App")

# Load the pre-trained DataFrame and model pipeline
with open('df1.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.markdown("Fill in the applicant's details to predict loan approval.")

# User inputs
no_of_dependents = st.slider('Choose Number of Dependents', 0, 5)
Education = st.selectbox('Choose Education', ['Graduated', 'Not Graduated'])
self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
income_annum = st.slider('Choose Annual Income', 0, 10000000)
loan_amount = st.slider('Choose Loan Amount', 0, 10000000)
loan_term = st.slider('Choose Loan Duration', 0, 20)
cibil_score = st.slider('Choose Cibil Score', 0, 1000)
residential_assets_value = st.slider('Choose Residential Assets Value', 0, 10000000)
commercial_assets_value = st.slider('Choose Commercial Assets Value', 0, 10000000)
luxury_assets_value = st.slider('Choose Luxury Assets Value', 0, 10000000)
bank_asset_value = st.slider('Choose Bank Asset Value', 0, 10000000)

button_clicked = st.button('Predict')

if button_clicked:
    data = [[
        no_of_dependents, Education, self_employed, income_annum,
        loan_amount, loan_term, cibil_score, residential_assets_value,
        commercial_assets_value, luxury_assets_value, bank_asset_value
    ]]
    columns = [
        'no_of_dependents', 'education', 'self_employed', 'income_annum',
        'loan_amount', 'loan_term', 'cibil_score', 'residential_assets_value',
        'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value'
    ]

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    # Make prediction
    prediction = pipeline.predict(one_df)

    # Show raw prediction (optional)
    st.text(f"Raw Prediction Value: {prediction[0]}")

    # Convert to readable text and display result
    if prediction[0] == 1:
        st.success("Prediction: Loan Approved")
    else:
        st.error("Prediction: Loan Not Approved")