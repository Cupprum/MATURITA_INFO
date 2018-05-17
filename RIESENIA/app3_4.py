import tkinter as tk
from tkinter import *
import random


def start_game(dic_numbers, counter, rounds_left, random_1, random_2):
    player1 = random_1.get()
    player2 = random_2.get()
    rounds_left = rounds_left.get()

    if player1 > player2:
        dic_numbers['p1'] += 1
        dic_numbers['p2'] -= 1

    elif player1 < player2:
        dic_numbers['p1'] -= 1
        dic_numbers['p2'] += 1

    else:
        dic_numbers['p1'] += 0.5
        dic_numbers['p2'] += 0.5

    counter += 1
    rounds_left -= 1

    score_var_p1.set(str(dic_numbers['p1']))
    score_var_p2.set(str(dic_numbers['p2']))
    score_var_round.set(counter)
    score_var_rounds_left.set(rounds_left)

    root.update_idletasks()


def set_rounds():
    score_var_rounds_left.set(set_number_rounds_entry.get())
    root.update_idletasks()


def new_round_p1(random_1):
    random_1.set(random.randint(1, 21))
    root.update_idletasks()


def new_round_p2(random_2):
    random_2.set(random.randint(1, 21))
    root.update_idletasks()


root = Tk()
root.title("GAME")
root.geometry('400x200')

score_var_p1 = StringVar()
score_var_p1.set('')
score_var_p2 = StringVar()
score_var_p2.set('')

score_var_round = IntVar()
score_var_round.set(0)
score_var_rounds_left = IntVar()
score_var_rounds_left.set(0)

random_1 = IntVar()
random_1.set(0)
random_2 = IntVar()
random_2.set(0)

dic_numbers = {'p1': 0, 'p2': 0}
counter = 0

p1_name = tk.Label(root, text='p1')
p1_name.grid(column=0, row=0)
p1_score = tk.Label(root, textvariable=score_var_p1)
p1_score.grid(column=0, row=1)
p1_button_start = tk.Button(root, text='Start',
                            command=lambda: new_round_p1(random_1))
p1_button_start.grid(column=0, row=2)
p1_actual_text = tk.Label(root, text='actual number')
p1_actual_text.grid(column=0, row=3)
p1_actual_var = tk.Label(root, textvariable=random_1)
p1_actual_var.grid(column=0, row=4)

p2_name = tk.Label(root, text='p2')
p2_name.grid(column=1, row=0)
p2_score = tk.Label(root, textvariable=score_var_p2)
p2_score.grid(column=1, row=1)
p2_button = tk.Button(root, text='Start',
                      command=lambda: new_round_p2(random_2))
p2_button.grid(column=1, row=2)

p2_actual_text = tk.Label(root, text='actual number')
p2_actual_text.grid(column=1, row=3)
p2_actual_var = tk.Label(root, textvariable=random_2)
p2_actual_var.grid(column=1, row=4)

round_name = tk.Label(root, text='round')
round_name.grid(column=2, row=0)
round_score = tk.Label(root, textvariable=score_var_round)
round_score.grid(column=2, row=1)

rounds_left = tk.Label(root, text='rounds left')
rounds_left.grid(column=2, row=2)
rounds_left_score = tk.Label(root, textvariable=score_var_rounds_left)
rounds_left_score.grid(column=2, row=3)

set_number_rounds_entry = tk.Entry(root, width=9)
set_number_rounds_entry.grid(column=3, row=0)
set_number_rounds_button = tk.Button(root, text='Potvrdit', command=set_rounds)
set_number_rounds_button.grid(column=3, row=1)

start_round = tk.Button(root, text='Start',
                        command=lambda: start_game(
                            dic_numbers,
                            counter,
                            score_var_rounds_left,
                            random_1,
                            random_2))
start_round.grid(column=3, row=2)

root.update_idletasks()

root.mainloop()
