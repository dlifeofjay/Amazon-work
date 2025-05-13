import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sys

model = joblib.load('amazon_mod.pkl')
le= joblib.load('amazon_le.pkl')

st.title('Amazon Transaction Status Estimator')

st.header('Transaction Status Predictor for Amazon')
st.subheader('input the features')

Product = st.selectbox('Product', options=['Running Shoes', 'Headphones', 'Smartwatch', 'T-Shirt',
       'Smartphone', 'Book', 'Jeans', 'Laptop', 'Washing Machine',
       'Refrigerator'])
Category = st.selectbox('Category', options=['Footwear', 'Electronics', 'Clothing', 'Books', 'Home Appliances'])
Total_Sales = st.number_input('Total Sales', min_value=10.0, max_value=10000.0, value=100.0)
Customer_Location = st.selectbox('Customer Location', options=['New York', 'San Francisco', 'Denver', 'Dallas', 'Houston',
       'Miami', 'Boston', 'Seattle', 'Los Angeles', 'Chicago'])
Payment_Method = st.selectbox('Payment Method', options=['Debit Card', 'Amazon Pay', 'Credit Card', 'PayPal', 'Gift Card'])


input_data = {
    'Product': Product,
    'Category': Category,
    'Total Sales': Total_Sales,
    'Customer Location': Customer_Location,
    'Payment Method': Payment_Method
}

def amazon_prediction(input_data):
    input_df = pd.DataFrame([input_data])
    cols = ['Product', 'Category', 'Customer Location', 'Payment Method']
    for col in cols:
        input_df[col] = le.fit_transform(input_df[col])

    prediction = model.predict(input_df)
    return prediction

if st.button('Check Status'):
    prediction = amazon_prediction(input_data)
    if prediction == 0:
        st.error('Transaction Cancelled')
    elif prediction == 1:
        st.success('Transaction Successful')
    else:
        st.warning('Transaction Pending')
else:
    st.info('Click the button to check the transaction status')