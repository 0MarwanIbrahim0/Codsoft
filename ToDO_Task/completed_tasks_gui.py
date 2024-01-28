import tkinter as tk

class CompletedTasksWindow:
    def __init__(self, completed_tasks):
        self.root = tk.Tk()
        self.root.title("Completed Tasks")

        self.completed_tasks = completed_tasks

        self.setup_gui()

    def setup_gui(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        title_label = tk.Label(frame, text="Completed Tasks", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)

        self.completed_listbox = tk.Listbox(frame, selectmode=tk.SINGLE, width=40, font=("Arial", 12))
        self.update_completed_listbox()
        self.completed_listbox.pack(pady=10)

        close_button = tk.Button(frame, text="Close", command=self.close_window, bg="#FF6347", fg="white", font=("Arial", 12, "bold"))
        close_button.pack(pady=10)

    def update_completed_listbox(self):
        self.completed_listbox.delete(0, tk.END)
        for task in self.completed_tasks:
            self.completed_listbox.insert(tk.END, task)

    def close_window(self):
        self.root.destroy()
