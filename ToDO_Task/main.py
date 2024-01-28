from todo_list import TodoList
from Main_todo_gui import StyledTodoListApp

if __name__ == "__main__":
    todo_list = TodoList()
    app = StyledTodoListApp(todo_list)
    app.run()
    