
import tkinter as tk
import csv
from datetime import datetime

FILENAME = "csv"

def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()

    if category and amount:
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), category, amount])
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            expenses = file.readlines()
    except FileNotFoundError:
        expenses = ["No expenses recorded.\n"]

    view_win = tk.Toplevel(root)
    for exp in expenses:
        tk.Label(view_win, text=exp.strip()).pack()

root = tk.Tk()
root.title("Simple Expense Tracker")

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="View Expenses", command=view_expenses).pack()

root.mainloop()