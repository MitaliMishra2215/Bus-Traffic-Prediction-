import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime, timedelta

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
st.title("🚌 Bus Arrival Time Prediction System")

st.write("Enter journey details:")

hour = st.slider("Departure Hour", 0, 23)
day = st.slider("Day", 1, 31)
month = st.slider("Month", 1, 12)
day_of_week = st.slider("Day of Week (0=Mon)", 0, 6)

# NEW INPUT (IMPORTANT 🔥)
base_time = st.number_input("Base Travel Time (minutes)", min_value=10, max_value=120, value=30)

if st.button("Predict Arrival Time"):
    input_data = [[hour, day, month, day_of_week]]
    
    # Predict traffic
    predicted_traffic = model.predict(input_data)[0]

    # Calculate delay based on traffic
    delay = predicted_traffic * 0.5   # simple assumption

    # Total travel time
    total_time = base_time + delay

    # Current time
    current_time = datetime.now()

    # Arrival time
    arrival_time = current_time + timedelta(minutes=total_time)

    # Output
    st.success(f"🚗 Predicted Traffic: {int(predicted_traffic)} vehicles")
    st.info(f"⏳ Estimated Delay: {int(delay)} minutes")
    st.success(f"🚌 Estimated Bus Arrival Time: {arrival_time.strftime('%H:%M:%S')}")