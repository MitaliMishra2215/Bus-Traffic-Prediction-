# 🚌 Bus Arrival Time Prediction System

## 📌 Project Overview

This project focuses on building a time-series based system that predicts the arrival time of buses using historical traffic data. The system first predicts traffic volume using a machine learning model and then estimates bus arrival time based on traffic conditions and base travel time.

## 🎯 Objective

Predict traffic volume using time-based features
Estimate bus arrival time using predicted traffic
Develop an interactive web application for real-time prediction

## 🧠 Methodology

### Step 1: Traffic Prediction

A Random Forest Regressor model is used to predict the number of vehicles based on hour, day, month, and day of week.

### Step 2: Arrival Time Estimation

The arrival time is calculated using:

Total Travel Time = Base Time + Traffic Delay

Where:
Base Time = User input (minutes)
Traffic Delay = Predicted Vehicles × 0.5

## ⚙️ Technologies Used

Python
Pandas
NumPy
Scikit-learn
Matplotlib
Streamlit

## 📊 Dataset Details

Dataset: Traffic dataset (CSV)
Records used: 5000

Features:
DateTime
Junction
Vehicles (Target Variable)
ID

## 🚀 How to Run the Project

### Install dependencies

pip install pandas numpy scikit-learn matplotlib streamlit

### Run Notebook

Open the notebook file and click Run All

### Run Streamlit App

streamlit run app.py

## 🖥️ Output

Predicted Traffic (Vehicles)
Estimated Delay
Predicted Bus Arrival Time

## Screenshots
<img width="1920" height="1080" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/2745d032-5877-46cb-b77b-d0aa96a41f2a" />
<img width="1920" height="1080" alt="Screenshot (66)" src="https://github.com/user-attachments/assets/9c9e105e-9316-48b8-9df4-b5e9719f98d2" />


## 📈 Model Performance

MAE: (add your value)
RMSE: (add your value)

## 📌 Conclusion

A time-series based machine learning system was developed to predict traffic volume and estimate bus arrival time. The model effectively captures traffic patterns and provides realistic arrival time predictions. The system is deployed using Streamlit, enabling real-time interaction.

## 👩‍💻 Author

Mitali Mishra
B.Tech IT (Data Analytics)
