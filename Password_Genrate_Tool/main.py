import tkinter as tk
from tkinter import scrolledtext
import string
import random


def password_generator(length, complx):
	len_password = length
	complex_degree = complx
	match complex_degree:
		case "numbers only":
			complex_degree = string.digits
		case "letters":
			complex_degree = string.ascii_letters
		case "letters & numbers":
			complex_degree = string.ascii_letters + string.digits
		case "special characters":
			complex_degree = string.punctuation + string.ascii_letters + string.digits
		case _:
			print("not matched")
	password = ''.join(random.choice(complex_degree) for i in range(len_password))
	return password


def generate_password():
	password = password_generator(length.get(), complx_var.get())
	result_text.delete(1.0, tk.END)
	result_text.insert(tk.END, password)


def copy_to_clipboard():
	generated_password = result_text.get(1.0, tk.END).strip()
	root.clipboard_clear()
	root.clipboard_append(generated_password)
	root.update()


root = tk.Tk()

root.title("Password Generator")
root.geometry("400x200")

label = tk.Label(root, text="Password Length:", font=("Arial", 10, "bold"))
label.grid(row=0, column=0)

length = tk.IntVar()
length_spinbox = tk.Spinbox(root, from_=8, to=26, textvariable=length)
length_spinbox.grid(row=0, column=1)

check_list = [1, 2, 3, 4]
text_radio = ["numbers only", "letters", "letters & numbers", "special characters"]
complx_var = tk.StringVar()

for i in range(4):
	option = tk.Radiobutton(root, text=text_radio[i], variable=complx_var, value=text_radio[i])
	option.grid(row=i + 1, column=0)

result_frame = tk.LabelFrame(root, text="Password Results", padx=5, pady=5)
result_frame.grid(row=1, column=1, rowspan=4, padx=10)

result_text = scrolledtext.ScrolledText(result_frame, width=30, height=4, wrap=tk.WORD)
result_text.pack(expand=True, fill=tk.BOTH)

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=5, column=1, pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=6, column=1, pady=5)

root.mainloop()
