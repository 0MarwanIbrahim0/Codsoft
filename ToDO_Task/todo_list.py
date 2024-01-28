class TodoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
        else:
            raise ValueError("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise ValueError("Invalid task index.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            completed_task = self.tasks[index]
            del self.tasks[index]
            self.completed_tasks.append(completed_task)
        else:
            raise ValueError("Invalid task index.")
