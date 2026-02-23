import csv
import random
from datetime import datetime
import os

def generate_sensor_reading():
    """
    Simulates a real-time industrial sensor.
    Generates a value, timestamps it, and appends it to the local CSV database.
    """
    file_path = 'sensor_data.csv'
    
    # Base configuration for simulation
    base_value = 280.0 
    noise = random.uniform(-5.0, 5.0) # Simulating environmental interference
    current_value = round(base_value + noise, 2)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Appending data to CSV (Local Database)
    try:
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, current_value])
        print(f"Log: Data Point Captured -> {current_value} at {timestamp}")
    except Exception as e:
        print(f"IO Error: Could not write to database. {e}")

if __name__ == "__main__":
    generate_sensor_reading()