import tkinter as tk
from tkinter import ttk


def button_click(number):
	current = entry_var.get()
	entry_var.set(current + str(number))


def clear_entry():
	entry_var.set("")


def calculate():
	try:
		expression = entry_var.get()
		result = eval(expression)
		entry_var.set(result)
	except Exception as e:
		entry_var.set("Error")


# Create main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

# Colors
bg_color = '#111111'
btn_bg_color = '#FFFFFF'
btn_fg_color = '#333333'


style = ttk.Style()
style.configure("TButton", padding=(5, 5, 5, 5), font=('Helvetica', 12), background=btn_bg_color, foreground=btn_fg_color)
style.configure("TEntry", padding=(5, 5, 5, 5), font=('Helvetica', 16), background=btn_bg_color, foreground=btn_fg_color)
style.configure("TLabel", padding=(5, 5, 5, 5), font=('Helvetica', 12), background=bg_color, foreground=btn_fg_color)

window.configure(bg=bg_color)

# Entry widget for user input
entry_var = tk.StringVar()
entry = ttk.Entry(window, textvariable=entry_var, justify='right', font=('Helvetica', 16))
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky='nsew')

# Button layout
buttons = [
	'7', '8', '9', '/',
	'4', '5', '6', '*',
	'1', '2', '3', '-',
	'0', '.', '+'
]

row_val = 1
col_val = 0

# Create numbered buttons
for button in buttons:
	ttk.Button(window, text=button, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val, pady=5, padx=5, sticky='nsew')
	col_val += 1
	if col_val > 3:
		col_val = 0
		row_val += 1

# Equals button
ttk.Button(window, text='=', command=calculate).grid(row=row_val, pady=5, padx=5, sticky='nsew')

# Clear button
ttk.Button(window, text='C', command=clear_entry).grid(row=row_val, column=col_val, pady=5, padx=5, sticky='nsew')



# Grid configuration
for i in range(5):
	window.grid_columnconfigure(i, weight=1)
	window.grid_rowconfigure(i, weight=1)

# Start the Tkinter event loop
window.mainloop()
