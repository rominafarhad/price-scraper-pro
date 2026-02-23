import tkinter as tk
from tkinter import messagebox
import subprocess

def run_ai_prediction():
    """Triggers the external AI prediction script."""
    try:
        # Running the AI module as a subprocess
        subprocess.run(["python", "ai_predictor.py"], check=True)
    except Exception as e:
        messagebox.showerror("System Error", f"Failed to execute AI module: {e}")

# --- GUI Application Setup ---
window = tk.Tk()
window.title("Smart Industrial Monitoring")
window.geometry("400x450")
window.configure(bg="#f8f9fa")

# Header Section
header = tk.Label(window, text="AI Monitoring Dashboard", 
                  font=("Helvetica", 16, "bold"), bg="#f8f9fa", fg="#2c3e50")
header.pack(pady=30)

# Main Action Button: AI Forecasting
btn_ai = tk.Button(window, 
                   text="3. RUN AI FORECASTING", 
                   command=run_ai_prediction, 
                   bg="#f1c40f", 
                   fg="#2c3e50", 
                   font=("Arial", 11, "bold"),
                   width=25, 
                   height=2,
                   relief="flat")
btn_ai.pack(pady=15)

# Footer Status
status = tk.Label(window, text="Status: Ready to analyze", bg="#f8f9fa", fg="#95a5a6")
status.pack(side="bottom", pady=20)

window.mainloop()