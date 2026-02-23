import pandas as pd
import matplotlib.pyplot as plt

def create_chart():
    print("Reading data from CSV...")
    try:
        # 1. Load data using pandas
        df = pd.read_csv('sensors_data.csv')
        
        # 2. Clean Price column: remove " Tomans" and "," then convert to number
        df['Price_Numeric'] = df['Price'].str.replace(' Tomans', '').str.replace(',', '').astype(float)
        
        # 3. Create the bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(df['Component Name'], df['Price_Numeric'], color='teal')
        
        # Add labels and title
        plt.xlabel('Sensors & Components', fontsize=12)
        plt.ylabel('Price (Tomans)', fontsize=12)
        plt.title('Price Analysis of Electronic Components', fontsize=14)
        plt.xticks(rotation=15) # Rotate names slightly for better reading
        
        # 4. Save and Show
        plt.tight_layout()
        plt.savefig('price_analysis_chart.png')
        print("✅ Success! Chart saved as 'price_analysis_chart.png'")
        plt.show()

    except Exception as e:
        print(f"Oops! Something went wrong: {e}")

if __name__ == "__main__":
    create_chart()