import tkinter as tk
import math

def calculate():
    x = float(entry_x.get())
    y = float(entry_y.get())
    choice = operation_var.get()

    if choice == "Addition":
        result = x + y
    elif choice == "Subtraction":
        result = x - y
    elif choice == "Multiplication":
        result = x * y
    elif choice == "Division":
        if y == 0:
            result = "Error: Division by zero"
        else:
            result = x / y
    elif choice == "Exponentiation":
        result = math.pow(x, y)
    else:
        result = "Invalid choice"

    result_label.config(text=f"Result: {result:.2f}")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry fields for x and y
entry_x = tk.Entry(window)
entry_x.pack()
entry_y = tk.Entry(window)
entry_y.pack()

# Sample buttons for base and exponent
base_button = tk.Button(window, text="Enter Base", command=lambda: entry_x.focus())
base_button.pack()
exponent_button = tk.Button(window, text="Enter Exponent", command=lambda: entry_y.focus())
exponent_button.pack()

# Operation dropdown
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]
operation_var = tk.StringVar(value=operations[0])
operation_menu = tk.OptionMenu(window, operation_var, *operations)
operation_menu.pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Result label
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Run the GUI
window.mainloop()
