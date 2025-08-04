import tkinter as tk
import math

# Colors and Styles
BG_COLOR = "#2E2E2E"
BTN_COLOR = "#4E4E4E"
BTN_HOVER = "#6E6E6E"
TEXT_COLOR = "#FFFFFF"
ENTRY_BG = "#1E1E1E"
FONT = ("Helvetica", 18)

# Functions
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get()
        expr = expr.replace("√", "math.sqrt")
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main Window
root = tk.Tk()
root.title("🧮 Stylish Calculator")
root.geometry("400x550")
root.configure(bg=BG_COLOR)

# Entry Display
entry = tk.Entry(root, font=("Consolas", 24), fg=TEXT_COLOR, bg=ENTRY_BG,
                 bd=0, insertbackground=TEXT_COLOR, justify='right')
entry.pack(padx=20, pady=20, ipady=15, fill="x")

# Button Layout
buttons = [
    ['(', ')', '√', 'C'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '%', '+'],
    ['**', '=', '', '']
]

def create_button(frame, text, command):
    if text == '':
        tk.Label(frame, width=6).pack(side='left', padx=5, pady=5)
        return
    btn = tk.Button(frame, text=text, font=FONT, fg=TEXT_COLOR,
                    bg=BTN_COLOR, activebackground=BTN_HOVER,
                    activeforeground=TEXT_COLOR, width=6, height=2,
                    relief="flat", command=command)
    btn.pack(side='left', padx=5, pady=5)

# Create Buttons
for row in buttons:
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack()
    for btn_text in row:
        if btn_text == '=':
            create_button(frame, btn_text, calculate)
        elif btn_text == 'C':
            create_button(frame, btn_text, clear)
        else:
            create_button(frame, btn_text, lambda x=btn_text: button_click(x))

# Run App
root.mainloop()
