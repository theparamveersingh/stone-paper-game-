import tkinter as tk
import random

CHOICES = {"Stone": -1, "Paper": 1, "Scissor": 0}
NAMES = {-1: "Stone", 0: "Scissor", 1: "Paper"}

score = {"You": 0, "Computer": 0, "Draw": 0}

def play(choice):
    you = CHOICES[choice]
    computer = random.choice([-1, 0, 1])

    if you == computer:
        result = "DRAW"
        score["Draw"] += 1
    elif (you == -1 and computer == 0) or (you == 1 and computer == -1) or (you == 0 and computer == 1):
        result = "YOU WIN!"
        score["You"] += 1
    else:
        result = "COMPUTER WINS"
        score["Computer"] += 1

    player_var.set(f"You: {choice}")
    computer_var.set(f"Computer: {NAMES[computer]}")
    result_var.set(result)
    you_score.set(str(score["You"]))
    draw_score.set(str(score["Draw"]))
    computer_score.set(str(score["Computer"]))

def reset():
    score.update({"You": 0, "Computer": 0, "Draw": 0})
    you_score.set(draw_score.set(computer_score.set("0")))
    player_var.set("You: —")
    computer_var.set("Computer: —")
    result_var.set("Choose your move")

root = tk.Tk()
root.title("Stone • Paper • Scissor")
root.geometry("620x560")
root.resizable(False, False)
root.configure(bg="#10131a")

title = tk.Label(root, text="STONE • PAPER • SCISSOR",
                 font=("Segoe UI", 24, "bold"), fg="#ffffff", bg="#10131a")
title.pack(pady=(28, 5))

tk.Label(root, text="Beat the computer if you can!",
         font=("Segoe UI", 11), fg="#9aa4b2", bg="#10131a").pack()

result_var = tk.StringVar(value="Choose your move")
player_var = tk.StringVar(value="You: —")
computer_var = tk.StringVar(value="Computer: —")

tk.Label(root, textvariable=result_var, font=("Segoe UI", 22, "bold"),
         fg="#63e6be", bg="#10131a").pack(pady=25)

info = tk.Frame(root, bg="#181d27")
info.pack(padx=45, fill="x")

tk.Label(info, textvariable=player_var, font=("Segoe UI", 13, "bold"),
         fg="white", bg="#181d27", width=22).grid(row=0, column=0, pady=18)
tk.Label(info, text="VS", font=("Segoe UI", 12, "bold"),
         fg="#687386", bg="#181d27").grid(row=0, column=1)
tk.Label(info, textvariable=computer_var, font=("Segoe UI", 13, "bold"),
         fg="white", bg="#181d27", width=22).grid(row=0, column=2, pady=18)

tk.Label(root, text="YOUR MOVE", font=("Segoe UI", 10, "bold"),
         fg="#9aa4b2", bg="#10131a").pack(pady=(30, 10))

buttons = tk.Frame(root, bg="#10131a")
buttons.pack()

for name in CHOICES:
    tk.Button(buttons, text=name, command=lambda n=name: play(n),
              font=("Segoe UI", 12, "bold"), width=12, height=2,
              bg="#252c39", fg="white", activebackground="#343d4d",
              activeforeground="white", relief="flat", cursor="hand2"
              ).pack(side="left", padx=7)

score_frame = tk.Frame(root, bg="#181d27")
score_frame.pack(pady=28, padx=45, fill="x")

you_score = tk.StringVar(value="0")
draw_score = tk.StringVar(value="0")
computer_score = tk.StringVar(value="0")

for col, label, var in [(0, "YOU", you_score), (1, "DRAW", draw_score), (2, "COMPUTER", computer_score)]:
    tk.Label(score_frame, text=label, font=("Segoe UI", 9, "bold"),
             fg="#8993a3", bg="#181d27").grid(row=0, column=col, padx=55, pady=(14, 2))
    tk.Label(score_frame, textvariable=var, font=("Segoe UI", 20, "bold"),
             fg="white", bg="#181d27").grid(row=1, column=col, padx=55, pady=(0, 14))

tk.Button(root, text="RESET SCORE", command=reset,
          font=("Segoe UI", 10, "bold"), bg="#e05252", fg="white",
          activebackground="#c94343", activeforeground="white",
          relief="flat", padx=18, pady=8, cursor="hand2").pack()

tk.Label(root, text="Made with Python + Tkinter",
         font=("Segoe UI", 9), fg="#5f6877", bg="#10131a").pack(side="bottom", pady=15)

root.mainloop()
