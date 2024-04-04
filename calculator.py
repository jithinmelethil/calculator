import tkinter as tk
from tkinter import ttk

def button_click(symbol):
    current = entry.get()
    if current == "0" and symbol != ".":
        entry.delete(0, tk.END)
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)
    entry.insert(tk.END, "0")

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=15, font=("Arial", 20), justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4)

style = ttk.Style()
style.configure('Orange.TButton', foreground='orange', background='orange', font=('Arial', 16))

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0),
]

for (text, row, col) in buttons:
    if text == '=':
        button = ttk.Button(root, text=text, style='Orange.TButton', command=evaluate)
    elif text == 'C':
        button = ttk.Button(root, text=text, style='Orange.TButton', command=clear)
    else:
        button = ttk.Button(root, text=text, style='Orange.TButton', command=lambda text=text: button_click(text))
    button.grid(row=row, column=col, sticky=tk.N+tk.S+tk.E+tk.W, padx=5, pady=5)

root.mainloop()
