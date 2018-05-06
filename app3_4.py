import tkinter as tk
from tkinter import *
import random
import time


def whole_game(dic_numbers, counter):
    player1 = random.randint(1, 21)
    print(f'p1: {player1}')

    player2 = random.randint(1, 21)
    print(f'p2: {player2}')

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

    score_var_p1.set(str(dic_numbers['p1']))
    score_var_p2.set(str(dic_numbers['p2']))
    score_var_round.set(str(counter))

    time.sleep(2)
    root.update_idletasks()


root = Tk()
root.title("GAME")
root.geometry('200x200')

dic_numbers = {'p1': 0, 'p2': 0}
counter = 0

score_var_p1 = StringVar()
score_var_p1.set('')
score_var_p2 = StringVar()
score_var_p2.set('')
score_var_round = StringVar()
score_var_round.set('')


p1_name = tk.Label(root, text='p1')
p1_name.grid(column=0, row=0)
p1_score = tk.Label(root, textvariable=score_var_p1)
p1_score.grid(column=0, row=1)

p2_name = tk.Label(root, text='p2')
p2_name.grid(column=1, row=0)
p2_score = tk.Label(root, textvariable=score_var_p2)
p2_score.grid(column=1, row=1)

round_name = tk.Label(root, text='round')
round_name.grid(column=2, row=0)
round_score = tk.Label(root, textvariable=score_var_round)
round_score.grid(column=2, row=1)

root.update_idletasks()

for x in range(5):
    whole_game(dic_numbers, counter)

root.mainloop()
