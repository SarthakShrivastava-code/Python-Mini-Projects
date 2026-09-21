
import tkinter as tk
from time import strftime

# Function to update time
def time():
    string = strftime('%H:%M:%S %p')  # Format: Hours:Minutes:Seconds AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update every 1 second

# Creat main window
root = tk.Tk()
root.title("Digital Watch")

# Styling the label
label = tk.Label(root, font=('calibri', 50, 'bold'),
                 background='black',
                 foreground='cyan')
label.pack(anchor='center')

time()  # Start the clock

root.mainloop()