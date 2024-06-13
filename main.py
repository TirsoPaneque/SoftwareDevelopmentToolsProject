# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np

@st.cache_data 
def load_data():
    df = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv')
    return df

df = load_data()

st.title('Vehicles in the US')

st.header("Exploratory Data Analysis of vehicles in the US")

st.sidebar.title('Filtering Options')

# Ok so here im trying to set up a sidebar like the one on the NBA player analysis and filling the NaN values in the year with the mean as i did in the EDA.ipynb
df['model_year'] = df['model_year'].fillna(df['model_year'].median())
df['model_year'] = df['model_year'].astype(int)
model_year = st.sidebar.selectbox('Vehicle Year', sorted(df['model_year'].unique()))

# Now im adding to the sidebar a button to select particular car models
sorted_unique_car_model = sorted(df['model'].unique())
sorted_unique_car_model.insert(0, 'All')
selected_model = st.sidebar.multiselect('Model', [car.lower() for car in sorted_unique_car_model])

df['odometer'] = df.groupby('price')['odometer'].apply(lambda x: x.fillna(x.mean())).reset_index(drop=True)
df['odometer'] = df['odometer'].fillna(df['odometer'].mean())
df['odometer'] = df['odometer'].astype(int)
min_mileage = int(df['odometer'].min())
max_mileage = int(df['odometer'].max())
selected_min_mileage, selected_max_mileage = st.sidebar.slider('Select Mileage Range', min_mileage, max_mileage, (min_mileage, max_mileage))

# Apply filters to the DataFrame
filtered_df = df[
    ((model_year == 'All') | (df['model_year'] == model_year)) &
    ((len(selected_model) == 0) | (df['model'].isin(selected_model))) &
    (df['odometer'] >= selected_min_mileage) &
    (df['odometer'] <= selected_max_mileage)
]

# Display the filtered DataFrame
st.write(filtered_df)




# Histogram of the model year
# st.pyplot(histogram.figure)

checkbox = st.sidebar.checkbox("Enable Scatter Plot")

if checkbox:
    # Show scatter plot if checkbox is checked
    scatter_plot = sns.scatterplot(data=filtered_df, x='price', y='odometer')
    st.pyplot(scatter_plot.figure)
else:
    # Show histogram by default
    histogram = sns.histplot(filtered_df, x='days_listed', bins=60)
    st.pyplot(histogram.figure) 
