from tkinter import *
import tkinter as tk


class Rectangle:
    def __init__(self, canvas, x1, y1, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + 1
        self.y2 = y1 + 1

        if color == 'c':
            self.color = 'red'
        else:
            self.color = 'blue'

        self.canvas = canvas
        self.rectangle = canvas.create_rectangle(self.x1, self.y1, self.x2,
                                                 self.y2, outline=self.color)


root = Tk()
root.title("Obrazok")
root.resizable(False, False)

canvas = tk.Canvas(root,
                   width=200,
                   height=200,
                   borderwidth=2,
                   relief="solid")
canvas.grid()

txt = open('../ZADANIA/VYBER_4/Zadanie_3_Uloha_1.txt', 'r').readlines()

first_line = txt[0].split(' ')

width = first_line[0]
height = first_line[1]

counter_y = 0
for x in txt[1:]:
    counter_x = 0
    for y in x:
        print(counter_x, counter_y, y)
        point = Rectangle(canvas, counter_x, counter_y, y)
        counter_x += 1
    counter_y += 1

root.mainloop()
