import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Let's track a specific component (e.g., a Power Transistor or Microcontroller)
def track_component_price():
    # Example: Searching for a specific part on a tech site
    url = "https://example-electronics-shop.com/product/stm32-micro" 
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # 1. Fetching the page
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 2. Extract price (This is a generic example, we'll tune it for a real site)
        # Assuming the price is in a tag like <span class="price">
        price_tag = soup.find("span", {"class": "price"})
        price = float(price_tag.text.replace("$", "").replace(",", ""))
        
        # 3. Save to a CSV file for our AI to learn
        with open('sensor_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            # Storing: Date, Price
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), price])
            
        print(f"Successfully tracked price: {price}")
        return price
    except Exception as e:
        print(f"Error during tracking: {e}")
        return None

if __name__ == "__main__":
    track_component_price()