import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

def predict_future_price():
    # 1. Simulating 100 days of price history for a sensor
    # In a real project, this data comes from your 'sensors_data.csv'
    days = np.array(range(1, 101)).reshape(-1, 1)
    
    # Let's assume price has a slight upward trend with some noise
    prices = 150000 + (days * 500) + np.random.normal(0, 5000, days.shape)

    # 2. Creating the AI Model (Linear Regression)
    # This is the same logic used in Smart Grids for Load Forecasting
    model = LinearRegression()
    model.fit(days, prices) # Training the brain!

    # 3. Predicting for the next 10 days
    future_days = np.array(range(101, 111)).reshape(-1, 1)
    predicted_prices = model.predict(future_days)

    # 4. Visualizing the Result
    plt.figure(figsize=(10, 5))
    plt.scatter(days, prices, color='blue', label='Actual Past Prices', s=10)
    plt.plot(future_days, predicted_prices, color='red', linewidth=3, label='AI Prediction')
    plt.title('Engineering Analysis: Sensor Price Forecasting')
    plt.xlabel('Days')
    plt.ylabel('Price (Tomans)')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('ai_prediction_chart.png')
    print("🚀 AI Prediction Complete! Chart saved.")
    plt.show()

if __name__ == "__main__":
    predict_future_price()