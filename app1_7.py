from tkinter import *
import tkinter as tk


class Rectangle:
    def __init__(self, canvas, act_rec):
        self.canvas = canvas

        self.x1 = act_rec[0]
        self.y1 = act_rec[1]
        self.x2 = act_rec[2]
        self.y2 = act_rec[3]

        self.rectangle = canvas.create_rectangle(self.x1, self.y1, self.x2,
                                                 self.y2, fill="red")


txt = open('../ZADANIA/VYBER_1/uloha_7.txt').readlines()

list_rectangles = []

for x in txt:
    list_rectangles.append(x[:-1])

root = Tk()
root.title("Pozemky")
root.resizable(False, False)

canvas = tk.Canvas(root, width=640, height=480, borderwidth=2, relief="solid")
canvas.grid()

for x in list_rectangles:
    act_rec = x.split(' ')
    act_rec = [int(x) for x in act_rec]

    new_rectangle = Rectangle(canvas, act_rec)
    print(new_rectangle)

root.mainloop()
