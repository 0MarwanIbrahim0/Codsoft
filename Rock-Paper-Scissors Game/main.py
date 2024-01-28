import tkinter as tk
import random
from PIL import Image, ImageTk

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You Lose!"

def animate_choice(user_choice, computer_choice):
    y = 0
    while y < 100:
        canvas.delete("all")
        canvas.create_image(150, y, image=images[user_choice], anchor=tk.CENTER, tags="user_choice")
        canvas.create_image(450, y, image=images[computer_choice], anchor=tk.CENTER, tags="computer_choice")
        y += 5
        root.update()
        root.after(50)

def make_choice(choice):
    global user_score, computer_score
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    animate_choice(choice, computer_choice)

    result = determine_winner(choice, computer_choice)

    user_choice_label.config(text=f"Your choice: {choice}", fg="blue")
    computer_choice_label.config(text=f"Computer choice: {computer_choice}", fg="red")
    result_label.config(text=result, fg="green")

    if 'win' in result:
        user_score += 1
    elif 'Lose' in result:
        computer_score += 1

    update_score()

def update_score():
    score_label.config(text=f"Your score: {user_score}, Computer score: {computer_score}", fg="purple")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg="lightgray")

canvas = tk.Canvas(root, width=600, height=200, bg="lightgray")
canvas.grid(row=0, column=0, columnspan=3)

rock_image = Image.open("rock.png")
paper_image = Image.open("paper.png")
scissors_image = Image.open("scissors.png")


rock_image = rock_image.resize((100, 100))
paper_image = paper_image.resize((100, 100))
scissors_image = scissors_image.resize((100, 100),)


rock_photo = ImageTk.PhotoImage(rock_image)
paper_photo = ImageTk.PhotoImage(paper_image)
scissors_photo = ImageTk.PhotoImage(scissors_image)

images = {'rock': rock_photo, 'paper': paper_photo, 'scissors': scissors_photo}

rock_button = tk.Button(root, image=rock_photo, command=lambda: make_choice('rock'), bg="lightblue")
paper_button = tk.Button(root, image=paper_photo, command=lambda: make_choice('paper'), bg="lightgreen")
scissors_button = tk.Button(root, image=scissors_photo, command=lambda: make_choice('scissors'), bg="lightyellow")

user_choice_label = tk.Label(root, text="Your choice: ", bg="lightgray")
computer_choice_label = tk.Label(root, text="Computer choice: ", bg="lightgray")
result_label = tk.Label(root, text="", bg="lightgray")
score_label = tk.Label(root, text="Your score: 0, Computer score: 0", bg="lightgray")

rock_button.grid(row=1, column=0, padx=10, pady=10)
paper_button.grid(row=1, column=1, padx=10, pady=10)
scissors_button.grid(row=1, column=2, padx=10, pady=10)
user_choice_label.grid(row=2, column=0, columnspan=3)
computer_choice_label.grid(row=3, column=0, columnspan=3)
result_label.grid(row=4, column=0, columnspan=3, pady=10)
score_label.grid(row=5, column=0, columnspan=3)

user_score = 0
computer_score = 0

root.mainloop()
