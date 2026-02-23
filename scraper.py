from bs4 import BeautifulSoup
import csv # Library to work with Excel-style files

def scrape_to_csv():
    # 1. Read the local file
    with open("test.html", "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    products = soup.find_all('div', class_='product')
    
    # 2. Prepare to save in a CSV file
    file_name = "sensors_data.csv"
    
    with open(file_name, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        # Write the Header (Top row of Excel)
        writer.writerow(["Component Name", "Price"])
        
        print("\n--- Extracting and Saving Data ---")
        for item in products:
            name = item.find('h2', class_='name').text
            price = item.find('p', class_='price').text
            
            # Save the row
            writer.writerow([name, price])
            print(f"Saved: {name}")

    print(f"\n✅ Done! Check your folder for '{file_name}'")

if __name__ == "__main__":
    scrape_to_csv()