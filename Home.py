import streamlit as st

st.set_page_config(
    page_title = 'Loan Approval',
    page_icon = 'chart_with_downwords_trends',
    layout = 'wide'

)
st.title('Loan Approval Dashboard')

st.image('loan_image.png.PNG')

st.markdown("""
Welcome to the Loan Approval Prediction App! 🏦

This tool helps predict whether a loan application is likely to be approved based on applicant details 
like income, credit score, employment, and more.

Use the sidebar to explore and filter the data.
""")
