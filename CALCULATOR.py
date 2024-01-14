import tkinter as tk
from tkinter import messagebox
def handle_key(event):
    key = event.char
    if key.isdigit() or key in "+-*/.":
        entry.insert(tk.END, key)
def clear_entry():
    entry.delete(0, tk.END)
def remove_single_element():
    current_text = entry.get()
    if current_text:
        entry.delete(len(current_text) - 1)
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))
root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('C', 4, 3),
    ('Del', 1, 4),
]
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 12),command=lambda t=text: handle_button_click(t))
    button.grid(row=row, column=column, padx=5, pady=5)
    button.bind("<Key>", handle_key)
root.bind("<Key>", handle_key)
def handle_button_click(button_text):
    if button_text == 'C':
        clear_entry()
    elif button_text == 'Del':
        remove_single_element()
    else:
        entry.insert(tk.END, button_text)
equal_button = tk.Button(root, text='=', width=5, height=2, font=("Arial", 12), command=calculate)
equal_button.grid(row=5, column=4, padx=5, pady=5)
equal_button.bind("<Key>", lambda e: calculate())
root.mainloop()