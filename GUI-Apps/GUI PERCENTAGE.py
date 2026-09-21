import tkinter as tk

def calculate_grade():
    try:
        score = float(entry.get())
        if score >= 90:
            result.set("Grade: A+")
        elif score >= 80:
            result.set("Grade: A")
        elif score >= 70:
            result.set("Grade: B")
        elif score >= 60:
            result.set("Grade: C")
        else:
            result.set("Grade: F")
    except ValueError:
        result.set("Invalid input!")

root = tk.Tk()
root.title("Student Grade Calculator")

tk.Label(root, text="Enter Marks (%):").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate", command=calculate_grade).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()