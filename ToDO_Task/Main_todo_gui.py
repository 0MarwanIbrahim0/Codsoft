import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel
from ttkthemes import ThemedTk

class StyledTodoListApp:
    def __init__(self, todo_list):
        self.root = ThemedTk(theme="Adapta")
        self.root.title("To-Do List App")
        self.todo_list = todo_list
        self.selected_task_index = None

        self.setup_gui()

    def setup_gui(self):
        self.root.geometry("400x600")
        self.root.configure(bg="black")

        frame = tk.Frame(self.root, bg="#4D4DFF", padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        greeting_label = tk.Label(frame, text="Good morning 🌅", bg="#4D4DFF", fg="white", font=("Arial", 14, "bold"))
        greeting_label.pack(pady=10)

        today_label = tk.Label(frame, text="Your tasks for today", bg="#4D4DFF", fg="white", font=("Arial", 12, "bold"))
        today_label.pack()

        self.task_listbox = tk.Listbox(frame, selectmode=tk.SINGLE, width=40, font=("Arial", 12))
        self.update_listbox()
        self.task_listbox.pack(pady=10)

        add_task_button = tk.Button(frame, text="+ Add a task 📝", command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        add_task_button.pack(pady=10)
        self.add_hover_effect(add_task_button, "#4CAF50")

        complete_task_button = tk.Button(frame, text="Complete Task ✔️", command=self.complete_selected_task, bg="#FFD700", fg="black", font=("Arial", 12, "bold"))
        complete_task_button.pack(pady=10)
        self.add_hover_effect(complete_task_button, "#FFD700")

        view_completed_button = tk.Button(frame, text="View Completed Tasks 📚", command=self.view_completed_tasks, bg="#1E90FF", fg="white", font=("Arial", 12, "bold"))
        view_completed_button.pack(pady=10)
        self.add_hover_effect(view_completed_button, "#1E90FF")

        self.task_listbox.bind('<ButtonRelease-1>', self.on_task_select)

    def add_hover_effect(self, widget,color):
        widget.bind("<Enter>", lambda event: self.on_enter(event, widget))
        widget.bind("<Leave>", lambda event: self.on_leave(event, widget,color))

    def on_enter(self, event, widget):
        widget['background'] = '#333333'

    def on_leave(self, event, widget, color):
        widget['background'] = color

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter a new task:")
        if task:
            self.todo_list.add_task(task)
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.todo_list.tasks):
            checkbox = "[✔️]" if i in self.todo_list.completed_tasks else "[ ]"
            self.task_listbox.insert(tk.END, f"{task} {checkbox}")

    def on_task_select(self, event):
        selected_task_index = self.task_listbox.curselection()
        self.selected_task_index = selected_task_index[0] if selected_task_index else None

    def complete_selected_task(self):
        if self.selected_task_index is not None:
            try:
                self.todo_list.complete_task(self.selected_task_index)
                self.update_listbox()
            except ValueError as e:
                messagebox.showwarning("Error", str(e))

    def view_completed_tasks(self):
        completed_tasks_window = Toplevel(self.root)
        completed_tasks_window.title("Completed Tasks")
        completed_tasks_window.geometry("300x300")

        completed_tasks_label = tk.Label(completed_tasks_window, text="Completed Tasks", font=("Arial", 14, "bold"))
        completed_tasks_label.pack(pady=10)

        completed_tasks_listbox = tk.Listbox(completed_tasks_window, selectmode=tk.SINGLE, width=30, font=("Arial", 12))
        for task in self.todo_list.completed_tasks:
            completed_tasks_listbox.insert(tk.END, task)
        completed_tasks_listbox.pack(pady=10)

    def run(self):
        self.root.mainloop()
