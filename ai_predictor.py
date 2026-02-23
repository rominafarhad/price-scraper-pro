import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import telebot

# --- Telegram API Configuration ---
BOT_TOKEN = "8658812603:AAGjimnoBlITXegCZXpsX_994itBFms_CVc"
CHAT_ID = "878211169"
bot = telebot.TeleBot(BOT_TOKEN)

def run_ai_analysis():
    """
    Loads historical sensor data, trains a Linear Regression model,
    and predicts future values with automated alerting.
    """
    try:
        # 1. Data Acquisition
        df = pd.read_csv('sensor_data.csv', names=['Time', 'Value'])
        
        # 2. Feature Engineering (Using index as time-series sequence)
        X = np.array(range(len(df))).reshape(-1, 1)
        y = df['Value'].values

        # 3. Model Training (Machine Learning)
        model = LinearRegression()
        model.fit(X, y)

        # 4. Forecasting: Predict the next 3 steps
        future_steps = 3
        future_index = np.array(range(len(df), len(df) + future_steps)).reshape(-1, 1)
        predictions = model.predict(future_index)

        # 5. Alert System: Check if predicted values exceed threshold
        threshold = 283.0
        if predictions[-1] > threshold:
            alert_msg = f"🚩 AI ALERT: Predicted value ({predictions[-1]:.2f}) exceeds threshold ({threshold})!"
            bot.send_message(CHAT_ID, alert_msg)
            print("Telegram Notification Dispatched! 🚨")

        # 6. Visualization (Data Science Dashboard)
        plt.style.use('ggplot')
        plt.figure(figsize=(10, 6))
        plt.plot(df.index, y, label='Historical Data', color='#3498db', marker='o')
        plt.plot(future_index, predictions, label='AI Forecast', color='#e74c3c', linestyle='--', marker='s')
        
        plt.title("Industrial Monitoring System - AI Forecasting")
        plt.xlabel("Sequence Number")
        plt.ylabel("Sensor Value (Units)")
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Analysis Failed: Ensure the CSV contains sufficient data points. Error: {e}")

if __name__ == "__main__":
    run_ai_analysis()