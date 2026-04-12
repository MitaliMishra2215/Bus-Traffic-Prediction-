import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("traffic.csv", nrows=5000)

# Preprocessing
df['DateTime'] = pd.to_datetime(df['DateTime'])
df.set_index('DateTime', inplace=True)

df['hour'] = df.index.hour
df['day'] = df.index.day
df['month'] = df.index.month
df['day_of_week'] = df.index.dayofweek

# Features
X = df[['hour', 'day', 'month', 'day_of_week']]
y = df['Vehicles']

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# UI
st.title("🚦 Bus Traffic Prediction System")

hour = st.slider("Hour", 0, 23)
day = st.slider("Day", 1, 31)
month = st.slider("Month", 1, 12)
day_of_week = st.slider("Day of Week (0=Mon)", 0, 6)

if st.button("Predict"):
    input_data = [[hour, day, month, day_of_week]]
    prediction = model.predict(input_data)
    st.success(f"Predicted Vehicles: {int(prediction[0])}")