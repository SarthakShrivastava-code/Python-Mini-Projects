import tkinter as tk
from math import pow

# Fun to cal EMI
def calculate():
    try:
        p = float(principal_entry.get())          # prin amount
        r = float(rate_entry.get()) / 100 / 12    # monthly interest rate
        n = int(years_entry.get()) * 12           # num of months

        if r == 0:
            emi = p / n
        else:
            emi = p * r * pow(1 + r, n) / (pow(1 + r, n) - 1)

        total_payment = emi * n
        total_interest = total_payment - p

        result_label.config(
            text=f"Monthly EMI: ₹{emi:,.2f}\n"
                 f"Total Payment: ₹{total_payment:,.2f}\n"
                 f"Total Interest: ₹{total_interest:,.2f}"
        )
    except:
        result_label.config(text="❌ Please enter valid numbers.")

# main win
root = tk.Tk()
root.title("Simple Loan Calculator")
root.geometry("350x300")
root.config(bg="#f8f8f8")

# Title
tk.Label(root, text="Loan Calculator", font=("Arial", 16, "bold"), bg="#f8f8f8").pack(pady=10)

# i/p fields
tk.Label(root, text="Loan Amount (₹):", bg="#f8f8f8").pack()
principal_entry = tk.Entry(root)
principal_entry.pack(pady=5)

tk.Label(root, text="Annual Interest Rate (%):", bg="#f8f8f8").pack()
rate_entry = tk.Entry(root)
rate_entry.pack(pady=5)

tk.Label(root, text="Loan Term (years):", bg="#f8f8f8").pack()
years_entry = tk.Entry(root)
years_entry.pack(pady=5)

# Button
tk.Button(root, text="Calculate", bg="#4caf50", fg="white", command=calculate).pack(pady=10)

# Result
result_label = tk.Label(root, text="", bg="#f8f8f8", font=("Arial", 11))
result_label.pack(pady=10)

# Run the app
root.mainloop()




