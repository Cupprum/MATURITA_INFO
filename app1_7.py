from tkinter import *
import tkinter as tk
import random
import time


class Point:
    def __init__(self, canvas, x, y, lst):
        self.canvas = canvas

        self.x = x
        self.y = y

        if x > lst[0] and x < lst[2] and y > lst[1] and y < lst[3]:
            self.color = 'green'
        else:
            self.color = 'red'

        self.rectangle = canvas.create_rectangle(self.x, self.y,
                                                 self.x + 1, self.y + 1,
                                                 outline=self.color)
        root.update_idletasks()


repetition = int(input('kolko krat mame opakovat : '))

txt = open('../ZADANIA/VYBER_1/uloha_7.txt').readlines()

list_rectangles = []

for x in txt:
    list_rectangles.append(x[:-1])

root = Tk()
root.title("Pozemky")
root.resizable(False, False)

canvas = tk.Canvas(root, width=640, height=480, borderwidth=2, relief="solid")
canvas.grid()

for _ in range(repetition):
    x = random.randint(0, 640)
    y = random.randint(0, 480)

    act_rec = list_rectangles[1].split(' ')
    act_rec = [int(x) for x in act_rec]

    new_rectangle = Point(canvas, x, y, act_rec)
    time.sleep(0)

root.mainloop()
