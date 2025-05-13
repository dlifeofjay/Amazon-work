import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('Amazon File Exploration')

uploaded_file = st.file_uploader('Upload an excel file', type='xlsx')

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        st.success('File Uploaded Successfully!')
        st.write('Data Preview::=')
        st.dataframe(df.head())

        st.sidebar.header('Filter Data')

        if 'Product' in df.columns and 'Category' in df.columns and 'Customer Location' in df.columns and 'Payment Method' in df.columns and 'Status' in df.columns:
            Product_filter = st.sidebar.multiselect('Select Product', options=df['Product'].dropna().unique(), default=df['Product'].dropna().unique())
            Category_filter = st.sidebar.multiselect('Select Category', options=df['Category'].dropna().unique(), default=df['Category'].dropna().unique())
            Customer_Location_filter = st.sidebar.multiselect('Select Customer Location', options=df['Customer Location'].dropna().unique(), default=df['Customer Location'].dropna().unique())
            Payment_Method_filter = st.sidebar.multiselect('Select Payment Method', options=df['Payment Method'].dropna().unique(), default=df['Payment Method'].dropna().unique())
            Status_filter = st.sidebar.multiselect('Select Status', options=df['Status'].dropna().unique(), default=df['Status'].dropna().unique())

            filtered_df = df[(df['Product'].isin(Product_filter)) & (df['Category'].isin(Category_filter)) & (df['Customer Location'].isin(Customer_Location_filter)) & (df['Payment Method'].isin(Payment_Method_filter)) & (df['Status'].isin(Status_filter))]

            st.subheader('Filtered Data')
            st.dataframe(filtered_df)

            allowed_columns = ["Category", "Product", "Customer Location", "Payment Method", "Status"]
            selectable_columns = [col for col in df.columns if col in allowed_columns]
            X_column_to_plot = st.selectbox("Select a column for the X axis", selectable_columns)
            column_to_plot = st.selectbox("Select a column for the Y axis", selectable_columns)
            st.subheader(f'Visualization of {X_column_to_plot} vs {column_to_plot}')
            fig, ax = plt.subplots()
            sns.countplot(data=filtered_df, x=X_column_to_plot, hue=column_to_plot, ax=ax)
            plt.xticks(rotation=90)
            st.pyplot(fig)

            selectable_columns = [col for col in df.columns if col in allowed_columns]
            column_to_plot = st.selectbox("Select a column for the pie chart", selectable_columns)
            pie_data = df[column_to_plot].value_counts()
            fig, ax = plt.subplots()
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
            st.pyplot(fig)
        else:
            st.warning("Dataset must include 'Sex' and 'Pclass' columns for filtering.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload an EXCEL file to get started.")