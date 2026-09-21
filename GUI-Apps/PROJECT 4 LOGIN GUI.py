
import tkinter as tk
from tkinter import messagebox

# Hardcoded credentials
USERNAME = "DHONI"
PASSWORD = "72011"

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == USERNAME and entered_password == PASSWORD:
        messagebox.showinfo("Login Success", f"Welcome, {USERNAME}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")
root.resizable(False, False)

# Username label and entry
tk.Label(root, text="Username:", font=("Arial", 12)).pack(pady=5)
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(pady=5)

# Password label and entry
tk.Label(root, text="Password:", font=("Arial", 12)).pack(pady=5)
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

# Login button
tk.Button(root, text="Login", font=("Arial", 12), command=login).pack(pady=10)

root.mainloop()