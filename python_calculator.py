import tkinter as tk
import math

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e1e")

entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=5, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def sin():
    try:
        result = math.sin(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def cos():
    try:
        result = math.cos(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

# Button style
btn_style = {
    "width": 5,
    "height": 2,
    "font": ('Arial', 12),
    "bg": "#333",
    "fg": "white"
}

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    else:
        action = lambda x=text: click(x)

    tk.Button(root, text=text, command=action, **btn_style).grid(row=row, column=col, padx=5, pady=5)

# Extra scientific buttons
tk.Button(root, text="C", command=clear, **btn_style).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="√", command=sqrt, **btn_style).grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text="sin", command=sin, **btn_style).grid(row=5, column=2, padx=5, pady=5)
tk.Button(root, text="cos", command=cos, **btn_style).grid(row=5, column=3, padx=5, pady=5)

# Keyboard support
def key_event(event):
    key = event.char
    if key in '0123456789+-*/.':
        click(key)
    elif key == '\r':
        calculate()
    elif key == '\x08':
        entry.delete(len(entry.get())-1, tk.END)

root.bind("<Key>", key_event)

root.mainloop()