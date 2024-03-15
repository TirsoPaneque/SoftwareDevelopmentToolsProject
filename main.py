# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

@st.cache  # Add caching for improved performance
def load_data():
    df = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv')
    return df

df = load_data()

st.header("Exploratory Data Analysis")

# Plotly Express histogram
histogram = px.histogram(df, x='column_name')  # Replace 'column_name' with the column i should plot
st.plotly_chart(histogram)

# Plotly Express scatter plot
scatter_plot = px.scatter(df, x='column1', y='column2', color='category_column')  # Adjust as per your dataset
st.plotly_chart(scatter_plot)

# Step 4: Add checkbox to change behavior of components
checkbox = st.checkbox("Enable Scatter Plot")

if checkbox:
    # Show scatter plot if checkbox is checked
    st.plotly_chart(scatter_plot)
else:
    # Show histogram by default
    st.plotly_chart(histogram)