import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to execute the scraper script
def run_scraper():
    try:
        # Runs the scraper.py file using the python interpreter
        subprocess.run(["python", "scraper.py"], check=True)
        messagebox.showinfo("Success", "Data scraped and saved to Excel successfully! ✅")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to execute the analyzer script
def run_analyzer():
    try:
        # Runs the analyzer.py file to generate the chart
        subprocess.run(["python", "analyzer.py"], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Could not create chart: {e}")

# --- UI Setup ---

# Create the main application window
window = tk.Tk()
window.title("Sensor Data Management Pro")
window.geometry("400x350")
window.configure(bg="#f4f4f4")

# App Header
header = tk.Label(window, text="Scraping & Analysis Tool", 
                  font=("Arial", 16, "bold"), bg="#f4f4f4", fg="#333")
header.pack(pady=25)

# Button to trigger Scraping
btn_scrape = tk.Button(window, text="1. Fetch Latest Prices", command=run_scraper, 
                       width=25, height=2, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"))
btn_scrape.pack(pady=10)

# Button to trigger Analysis/Chart
btn_analyze = tk.Button(window, text="2. Show Price Analysis", command=run_analyzer, 
                        width=25, height=2, bg="#3498db", fg="white", font=("Arial", 10, "bold"))
btn_analyze.pack(pady=10)

# Footer label
footer = tk.Label(window, text="Ready to process data", bg="#f4f4f4", fg="#888")
footer.pack(side="bottom", pady=10)

# Start the GUI event loop
window.mainloop()