import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def run_ai_analysis():
    print("🤖 AI Analysis started (Offline Mode)...")
    try:
        # 1. Data Acquisition from your CSV
        df = pd.read_csv('sensor_data.csv', names=['Time', 'Value'])
        
        # 2. Preparation
        X = np.array(range(len(df))).reshape(-1, 1)
        y = df['Value'].values

        # 3. AI Model Training
        model = LinearRegression()
        model.fit(X, y)

        # 4. Forecasting the next 3 points
        future_index = np.array(range(len(df), len(df) + 3)).reshape(-1, 1)
        predictions = model.predict(future_index)

        # 5. Local Alert (Printing to Terminal instead of Telegram)
        threshold = 283.0
        if predictions[-1] > threshold:
            print(f"⚠️ LOCAL ALERT: Predicted value ({predictions[-1]:.2f}) exceeds threshold!")
        else:
            print(f"✅ Trend is stable. Predicted: {predictions[-1]:.2f}")

        # 6. Visualization
        plt.style.use('ggplot')
        plt.figure(figsize=(10, 6))
        plt.plot(df.index, y, label='Actual Sensor Data', marker='o', color='blue')
        plt.plot(future_index, predictions, label='AI Forecast', linestyle='--', marker='s', color='red')
        
        plt.title("Industrial Monitoring - Offline AI Model")
        plt.xlabel("Reading Sequence")
        plt.ylabel("Value")
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"❌ Error: {e}. Make sure you have enough data in sensor_data.csv")

if __name__ == "__main__":
    run_ai_analysis()