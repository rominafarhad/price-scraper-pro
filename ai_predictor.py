import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import telebot
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = "878211169"

def run_ai_analysis():
    if not BOT_TOKEN:
        print("❌ Error: Token not found in .env file!")
        return

    try:
        # Connect Bot
        bot = telebot.TeleBot(BOT_TOKEN)
        
        # Data Acquisition
        df = pd.read_csv('sensor_data.csv', names=['Time', 'Value'])
        X = np.array(range(len(df))).reshape(-1, 1)
        y = df['Value'].values

        # AI Prediction
        model = LinearRegression()
        model.fit(X, y)
        future_index = np.array(range(len(df), len(df) + 3)).reshape(-1, 1)
        predictions = model.predict(future_index)

        # Alert if trend is high
        if predictions[-1] > 283.0:
            bot.send_message(CHAT_ID, f"🚀 AI Predicts price hike to: {predictions[-1]:.2f}")
            print("Alert Sent! 🚨")

        # Plotting
        plt.plot(df.index, y, label='History')
        plt.plot(future_index, predictions, 'r--', label='AI Forecast')
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    run_ai_analysis()