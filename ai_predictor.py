import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def run_ai_analysis():
    """
    Advanced Industrial AI Predictor (Offline Version)
    - Loads sensor data
    - Trains a Linear Regression model
    - Predicts the next 10 future points
    """
    print("🤖 AI Analysis Engine Started...")
    
    try:
        # 1. Load data from local CSV
        # We assume columns are [Timestamp, Value]
        df = pd.read_csv('sensor_data.csv', names=['Time', 'Value'])
        
        if len(df) < 5:
            print("❌ Error: Not enough data points. Please run the sensor_producer first.")
            return

        # 2. Data Preparation (Feature Engineering)
        X = np.array(range(len(df))).reshape(-1, 1)
        y = df['Value'].values

        # 3. Initialize and Train the AI Model
        model = LinearRegression()
        model.fit(X, y)

        # 4. Long-term Forecasting (Predicting next 10 points)
        future_points = 10 
        future_index = np.array(range(len(df), len(df) + future_points)).reshape(-1, 1)
        predictions = model.predict(future_index)

        # 5. Smart Threshold Check (Local Console Alert)
        limit = 283.0
        latest_pred = predictions[-1]
        print("-" * 30)
        print(f"Current Data Points: {len(df)}")
        print(f"AI Prediction for step {len(df) + future_points}: {latest_pred:.2f}")
        
        if latest_pred > limit:
            print(f"⚠️  WARNING: AI predicts a breach of {limit} in the near future!")
        else:
            print("✅ Status: System trend remains within safe limits.")
        print("-" * 30)

        # 6. Professional Visualization
        plt.style.use('dark_background') # Using a professional dark theme
        plt.figure(figsize=(12, 6))
        
        # Plotting Historical Data
        plt.plot(df.index, y, label='Historical Sensor Readings', color='#3498db', marker='o', markersize=4)
        
        # Plotting AI Forecast
        plt.plot(future_index, predictions, label=f'AI Forecast ({future_points} steps)', 
                 color='#e74c3c', linestyle='--', marker='s', markersize=5)
        
        # UI Polish
        plt.title("Industrial Sensor Monitoring & Advanced Prediction", fontsize=14, color='white')
        plt.xlabel("Reading Sequence", fontsize=12)
        plt.ylabel("Value (Units)", fontsize=12)
        plt.axhline(y=limit, color='yellow', linestyle=':', label=f'Safety Limit ({limit})')
        plt.legend()
        plt.grid(alpha=0.2)
        
        print("📊 Opening visualization window...")
        plt.show()

    except FileNotFoundError:
        print("❌ Error: 'sensor_data.csv' not found. Run your data generator script first!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_ai_analysis()