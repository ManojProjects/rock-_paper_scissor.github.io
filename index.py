import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.resizable(False, False)

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    messagebox.showinfo("Result",
                        f"Your choice: {user_choice}\n"
                        f"Computer's choice: {computer_choice}\n\n"
                        f"{result}")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=30)

rock_btn = tk.Button(btn_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="Scissors", font=("Arial", 14), width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

exit_btn = tk.Button(root, text="Exit", font=("Arial", 12), bg="#ff4d4d", fg="white", width=10, command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()
