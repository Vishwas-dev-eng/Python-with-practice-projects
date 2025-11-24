import tkinter as tk
import random

def play(choice):
    choices = {"Snake": 1, "Water": -1, "Gun": 0}
    reverse = {1: "Snake", -1: "Water", 0: "Gun"}

    user_val = choices[choice]
    comp_val = random.choice([-1, 0, 1])

    user_choice_label.config(text=f"You: {choice}")
    comp_choice_label.config(text=f"Computer: {reverse[comp_val]}")

    if user_val == comp_val:
        result_label.config(text="Result: Draw", fg="blue")
    elif (comp_val == -1 and user_val == 1) or \
         (comp_val == 1 and user_val == 0) or \
         (comp_val == 0 and user_val == -1):
        result_label.config(text="Result: You Win!", fg="green")
    else:
        result_label.config(text="Result: You Lose!", fg="red")

root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("350x350")
root.config(bg="#1e1e1e")

heading = tk.Label(root, text="Snake Water Gun", font=("Arial", 20, "bold"), bg="#1e1e1e", fg="white")
heading.pack(pady=15)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Snake", font=("Arial", 14), width=10, command=lambda: play("Snake")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Water", font=("Arial", 14), width=10, command=lambda: play("Water")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Gun", font=("Arial", 14), width=10, command=lambda: play("Gun")).grid(row=0, column=2, padx=10)

user_choice_label = tk.Label(root, text="You:", font=("Arial", 14), bg="#1e1e1e", fg="white")
user_choice_label.pack(pady=5)

comp_choice_label = tk.Label(root, text="Computer:", font=("Arial", 14), bg="#1e1e1e", fg="white")
comp_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Result:", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="white")
result_label.pack(pady=15)

root.mainloop()
