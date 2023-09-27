
import tkinter as tk
import string
import random



def generate_password():
    password_length = int(length_entry.get())

    

    password_chars = string.ascii_letters
    if include_numbers.get():
        password_chars += string.digits

        
    if include_special_chars.get():
        password_chars += string.punctuation
        

    password = ''.join(random.choice(password_chars) for _ in range(password_length))

    password_label.config(text=password)
    

root = tk.Tk()
root.title("Password Generator")
root.geometry("320x200")


include_numbers = tk.BooleanVar()
include_special_chars = tk.BooleanVar()


length_label = tk.Label(root, text="Password length:", font=("Arial", 14))
length_label.pack(pady=5)


length_entry = tk.Entry(root, font=("Arial", 14))

length_entry.pack(pady=10)


generate_button = tk.Button(root, text="Generate", font=("Arial", 14), command=generate_password)
generate_button.pack(pady=10)



password_label = tk.Label(root, text="", font=("Arial", 16))
password_label.pack(pady=10)


root.mainloop()
