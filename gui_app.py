import tkinter as tk
from tkinter import messagebox
import subprocess

# --- Functions ---
def run_scraper():
    try:
        subprocess.run(["python", "scraper.py"], check=True)
        messagebox.showinfo("Success", "Data updated! ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Scraper failed: {e}")

def run_analyzer():
    try:
        subprocess.run(["python", "analyzer.py"], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Analyzer failed: {e}")

def run_ai_prediction():
    try:
        # This calls your new AI script
        subprocess.run(["python", "ai_predictor.py"], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"AI module failed: {e}")

# --- UI Setup ---
window = tk.Tk()
window.title("Engineering Smart Monitor")
window.geometry("400x480")
window.configure(bg="#f0f2f5")

header = tk.Label(window, text="AI-Powered Sensor Tool", 
                  font=("Arial", 16, "bold"), bg="#f0f2f5", fg="#1a73e8")
header.pack(pady=25)

# Button 1
btn_scrape = tk.Button(window, text="1. Update Latest Data", command=run_scraper, 
                       width=25, height=2, bg="#34a853", fg="white", font=("Arial", 10, "bold"))
btn_scrape.pack(pady=10)

# Button 2
btn_analyze = tk.Button(window, text="2. Show Current Analysis", command=run_analyzer, 
                        width=25, height=2, bg="#4285f4", fg="white", font=("Arial", 10, "bold"))
btn_analyze.pack(pady=10)

# Button 3: THE AI BUTTON!
btn_ai = tk.Button(window, text="3. AI Future Forecasting", command=run_ai_prediction, 
                        width=25, height=2, bg="#fbbc05", fg="black", font=("Arial", 10, "bold"))
btn_ai.pack(pady=10)

footer = tk.Label(window, text="Status: Connected to AI Engine", bg="#f0f2f5", fg="#5f6368")
footer.pack(side="bottom", pady=20)

window.mainloop()