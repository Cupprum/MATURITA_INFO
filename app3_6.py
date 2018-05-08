from tkinter import *
import tkinter as tk


class Rectangle:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_rectangle(self.x1, self.y1, self.x2,
                                            self.y2, fill="red")


root = Tk()
root.title("Obdlzniky")
root.resizable(False, False)

canvas = tk.Canvas(root, width=500, height=500, borderwidth=2, relief="solid")
canvas.grid()

txt = open('../ZADANIA/Zadanie_6_Uloha_1.txt', 'r').readlines()

for x in txt:
    temporary = x.split(' ')
    temporary = list(map(int, temporary))

    x1 = temporary[0]
    x2 = temporary[2]
    y1 = temporary[1]
    y2 = temporary[3]

    rec = Rectangle(canvas, x1, y1, x2, y2)

root.mainloop()
