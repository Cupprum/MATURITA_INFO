import tkinter as tk
from tkinter import *
import random
import time


def whole_game(dic_numbers):
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

    score_var_p1.set(str(dic_numbers['p1']))
    score_var_p2.set(str(dic_numbers['p2']))

    time.sleep(2)


root = Tk()
root.title("GAME")
root.geometry('200x200')

dic_numbers = {'p1': 0, 'p2': 0}

score_var_p1 = StringVar()
score_var_p1.set('heloo')
score_var_p2 = StringVar()
score_var_p2.set('hola')


p1_name = tk.Label(root, text='p1')
p1_name.grid(column=0, row=0)
p1_score = tk.Label(root, textvariable=score_var_p1)
p1_score.grid(column=0, row=1)

p2_name = tk.Label(root, text='p2')
p2_name.grid(column=1, row=0)
p2_score = tk.Label(root, textvariable=score_var_p2)
p2_score.grid(column=1, row=1)

for x in range(5):
    whole_game(dic_numbers)

root.mainloop()
