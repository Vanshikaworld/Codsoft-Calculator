

import tkinter as tk
from tkinter import messagebox, ttk

def calculate():
    try:
        input1 = float(entry1.get())
        input2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            ans = input1 + input2
        elif operator == "-":
            ans = input1 - input2
        elif operator == "*":
            ans = input1 * input2
        elif operator == "/":
            if input2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            ans = input1 / input2
        else:
            messagebox.showerror("Error", "Please select a valid operator (+, -, *, /).")
            return

        result_var.set(ans)
        history_listbox.insert(tk.END, f"{input1} {operator} {input2} = {ans}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_var.set("")

def create_tooltip(widget, text):
    tooltip = tk.Label(widget, text=text, background="yellow", relief="solid", borderwidth=1, wraplength=150)
    tooltip.place_forget()

    def show_tooltip(event):
        tooltip.place(x=event.x_root - widget.winfo_rootx() + 20, y=event.y_root - widget.winfo_rooty() + 20)

    def hide_tooltip(event):
        tooltip.place_forget()

    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)

# Create the main window
root = tk.Tk()
root.title(" Calculator")
root.geometry("400x400")
root.resizable(False, False)

# Create StringVar for the result
result_var = tk.StringVar()

# Create entry fields and labels
label1 = ttk.Label(root, text="Enter your first input Number:")
label1.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry1 = ttk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)
create_tooltip(entry1, "Enter the first number")

label2 = ttk.Label(root, text="Enter your second input Number:")
label2.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry2 = ttk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)
create_tooltip(entry2, "Enter the second number")


label3 = ttk.Label(root, text="Select the arithmetic operation:")
label3.grid(row=2, column=0, padx=10, pady=5, sticky="e")
operator_var = tk.StringVar()
operator_menu = ttk.Combobox(root, textvariable=operator_var, values=["+", "-", "*", "/"])
operator_menu.grid(row=2, column=1, padx=10, pady=5)
create_tooltip(operator_menu, "Select an arithmetic operation")


result_label = ttk.Label(root, text="Result:")
result_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
result_entry = ttk.Entry(root, textvariable=result_var, state="readonly")
result_entry.grid(row=3, column=1, padx=10, pady=5)
create_tooltip(result_entry, "The result will be displayed here")

# Create the calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0, padx=10, pady=10)

# Create the clear button
clear_button = ttk.Button(root, text="Clear", command=clear)
clear_button.grid(row=4, column=1, padx=10, pady=10)

# Create a listbox to display calculation history
history_label = ttk.Label(root, text="History:")
history_label.grid(row=5, column=0, padx=10, pady=5, sticky="n")
history_listbox = tk.Listbox(root, height=10, width=40)
history_listbox.grid(row=5, column=1, padx=10, pady=5)

# Add a scrollbar to the history listbox
scrollbar = ttk.Scrollbar(root)
scrollbar.grid(row=5, column=2, sticky='ns')
history_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=history_listbox.yview)

# Run the main loop
root.mainloop()

