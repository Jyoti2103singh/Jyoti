import tkinter as tk
import random
import string
from tkinter import messagebox

# Password generation logic
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Length should be at least 4.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_output.config(state="normal")
        password_output.delete(0, tk.END)
        password_output.insert(0, password)
        password_output.config(state="readonly")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    password = password_output.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x300")
root.configure(bg="#2b2b2b")

# Title Label
tk.Label(root, text="Random Password Generator", font=("Helvetica", 18, "bold"),
         bg="#2b2b2b", fg="white").pack(pady=15)

# Length Input
tk.Label(root, text="Enter Password Length:", font=("Helvetica", 12),
         bg="#2b2b2b", fg="white").pack()
length_entry = tk.Entry(root, font=("Helvetica", 14), width=10, justify='center')
length_entry.pack(pady=5)

# Generate Button
tk.Button(root, text="Generate", font=("Helvetica", 12, "bold"),
          bg="#4CAF50", fg="white", padx=10, pady=5,
          command=generate_password).pack(pady=10)

# Password Output
password_output = tk.Entry(root, font=("Helvetica", 14), width=30, justify='center',
                           state='readonly', readonlybackground="#444", fg="white")
password_output.pack(pady=10)

# Copy Button
tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 12),
          bg="#2196F3", fg="white", command=copy_to_clipboard).pack(pady=5)

# Run the app
root.mainloop()
