import tkinter as tk
import random

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def get_result(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == 'Rock' and computer == 'Scissors') or \
         (user == 'Paper' and computer == 'Rock') or \
         (user == 'Scissors' and computer == 'Paper'):
        return "You Win!"
    else:
        return "You Lose!"

def play(user_choice):
    computer_choice = get_computer_choice()
    result = get_result(user_choice, computer_choice)

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

    global user_score, comp_score
    if "Win" in result:
        user_score += 1
    elif "Lose" in result:
        comp_score += 1

    score_label.config(text=f"You: {user_score}  |  Computer: {comp_score}")

user_score = 0
comp_score = 0

root = tk.Tk()
root.title("Rock Paper Scissors Game")

title = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20))
title.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Rock", width=12, command=lambda: play('Rock')).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Paper", width=12, command=lambda: play('Paper')).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Scissors", width=12, command=lambda: play('Scissors')).grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

score_label = tk.Label(root, text="You: 0  |  Computer: 0", font=("Arial", 14), fg="green")
score_label.pack()

root.mainloop()
