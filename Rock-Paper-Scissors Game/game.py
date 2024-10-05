import random
import tkinter as tk
from tkinter import messagebox

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle button click for user's choice
def play(user_choice):
    global user_score, computer_score
    
    # Computer makes a random choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    
    # Update result label
    result_label.config(text=f"You chose: {user_choice.capitalize()}\nComputer chose: {computer_choice.capitalize()}\n{result}")
    
    # Update the score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    # Update the score label
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

    # Check if anyone has reached the final score
    if user_score == 5:
        messagebox.showinfo("Game Over", "Congratulations! You won the game!")
        reset_game()
    elif computer_score == 5:
        messagebox.showinfo("Game Over", "Oops! The computer won the game.")
        reset_game()

# Function to reset the game when it ends
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score - You: 0, Computer: 0")
    result_label.config(text="Make your choice!")

# Function to exit the game
def exit_game():
    root.quit()

# Initialize score variables
user_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
root.config(bg='#F5F5DC')  # Light beige background color

# Create UI elements
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 24, "bold"), bg='#F5F5DC', fg='#333333')
title_label.pack(pady=20)

result_label = tk.Label(root, text="Make your choice!", font=("Arial", 14), bg='#F5F5DC', fg='#333333')
result_label.pack(pady=10)

# Create buttons for user choices with attractive colors and layout
button_frame = tk.Frame(root, bg='#F5F5DC')
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, bg='#FF4500', fg='white', command=lambda: play('rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10, bg='#4682B4', fg='white', command=lambda: play('paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14), width=10, bg='#32CD32', fg='white', command=lambda: play('scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Label to display the score
score_label = tk.Label(root, text="Score - You: 0, Computer: 0", font=("Arial", 12), bg='#F5F5DC', fg='#333333')
score_label.pack(pady=20)

# Exit button with a different color
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), width=10, bg='#FF6347', fg='white', command=exit_game)
exit_button.pack(pady=20)

# Start the main event loop
root.mainloop()
