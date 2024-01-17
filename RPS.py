import tkinter as tk
from tkinter import messagebox
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
--'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.configure(bg='black')  # Set the background color to black

user_score = 0
computer_score = 0
round_number = 1

def play_game(user_choice):
    global user_score, computer_score, round_number
    computer_choice = random.randint(0, 2)

    if user_choice == computer_choice:
        result = "It's a draw"
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose"
        computer_score += 1

    update_display(user_choice, computer_choice, result)
    round_number += 1

def update_display(user_choice, computer_choice, result):
    user_image_label.config(text=game_images[user_choice], font=("Courier", 14), bg='black', fg='white')
    computer_image_label.config(text=game_images[computer_choice], font=("Courier", 14), bg='black', fg='white')
    result_label.config(text=result, font=("Courier", 14), bg='black', fg='white')
    score_label.config(text=f"Round: {round_number}  |  You: {user_score}  |  Computer: {computer_score}", font=("Courier", 14), bg='black', fg='white')

user_image_label = tk.Label(root, text="", bg='black', fg='white')
computer_image_label = tk.Label(root, text="", bg='black', fg='white')
result_label = tk.Label(root, text="", bg='black', fg='white')
score_label = tk.Label(root, text="Round: 1  |  You: 0  |  Computer: 0", bg='black', fg='white')

user_image_label.grid(row=0, column=0, padx=20, pady=20)
computer_image_label.grid(row=0, column=1, padx=20, pady=20)
result_label.grid(row=1, column=0, columnspan=2, pady=20)
score_label.grid(row=2, column=0, columnspan=2, pady=20)

rock_btn = tk.Button(root, text="Rock", command=lambda: play_game(0), bg='black', fg='white')
paper_btn = tk.Button(root, text="Paper", command=lambda: play_game(1), bg='black', fg='white')
scissors_btn = tk.Button(root, text="Scissors", command=lambda: play_game(2), bg='black', fg='white')
exit_btn = tk.Button(root, text="Exit", command=root.destroy, bg='black', fg='white')

rock_btn.grid(row=3, column=0, pady=20)
paper_btn.grid(row=3, column=1, pady=20)
scissors_btn.grid(row=3, column=2, pady=20)
exit_btn.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
