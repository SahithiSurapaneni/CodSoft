import tkinter as tk
from math import factorial, sqrt

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, font=("Arial", 20), bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "!", "+",
    "sqrt", "C", "=",
]

row, col = 1, 0
for button in buttons:
    btn = tk.Button(root, text=button, font=("Arial", 16), padx=20, pady=10)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", on_click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
