import tkinter as tk
from tkinter import messagebox

# Function to calculate area
def calculate_area():
    selected_shape = shape_var.get()
    try:
        if selected_shape == "Triangle":
            base = float(entry1.get())
            height = float(entry2.get())
            area = (base * height) / 2
            result_label.config(text=f"Area of Triangle: {area:.2f} units²")
        elif selected_shape == "Square":
            side = float(entry1.get())
            area = side ** 2
            result_label.config(text=f"Area of Square: {area:.2f} units²")
        elif selected_shape == "Circle":
            radius = float(entry1.get())
            area = 3.14159 * (radius ** 2)
            result_label.config(text=f"Area of Circle: {area:.2f} units²")
        else:
            result_label.config(text="Please select a valid shape.")
    except ValueError:
        messagebox.showerror("Error", "Please enter numeric values only.")

# Setting up the main window
root = tk.Tk()
root.title("Area Calculator")
root.geometry("400x250")

# Dropdown menu for shapes
shape_var = tk.StringVar(value="Select a Shape")
shape_menu = tk.OptionMenu(root, shape_var, "Triangle", "Square", "Circle")
shape_menu.grid(row=0, column=1, pady=10)

# Input labels and fields
label1 = tk.Label(root, text="Input 1 (Base/Side/Radius):")
label1.grid(row=1, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

label2 = tk.Label(root, text="Input 2 (Height for Triangle):")
label2.grid(row=2, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate_area)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result display
result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
