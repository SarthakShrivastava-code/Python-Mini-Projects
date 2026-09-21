
import tkinter as tk
import random

# Function to toss coin
def toss_coin():
    result = random.choice(["Heads", "Tails"])
    label_result.config(text=f"Result: {result}")

# Create main window
root = tk.Tk()
root.title("Coin Toss")
root.geometry("300x200")

# Label
label_title = tk.Label(root, text="Toss a Coin", font=("Arial", 16))
label_title.pack(pady=10)

label_result = tk.Label(root, text="Result: ", font=("Arial", 14))
label_result.pack(pady=10)

# Button
btn_toss = tk.Button(root, text="Toss", font=("Arial", 14), command=toss_coin)
btn_toss.pack(pady=10)

# Run the GUI loop
root.mainloop()