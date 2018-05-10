from tkinter import *
import tkinter as tk
import cmath
import math


class Rectangle:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.canvas = canvas
        self.rectangle = canvas.create_rectangle(self.x1, self.y1, self.x2,
                                                 self.y2, fill="red")


class Polygon:
    def __init__(self, canvas, x1, y1, x2, y2, alfa):
        cangle = cmath.exp(math.radians(-alfa) * 1j)
        center = complex(x1, y2)

        pd = cangle * (complex(x2, y2) - center) + center
        ph = cangle * (complex(x2, y1) - center) + center
        lh = cangle * (complex(x1, y1) - center) + center

        self.x1 = x1
        self.y1 = y2
        self.x2 = pd.real
        self.y2 = pd.imag
        self.x3 = ph.real
        self.y3 = ph.imag
        self.x4 = lh.real
        self.y4 = lh.imag

        self.canvas = canvas
        self.polygon = canvas.create_polygon(self.x1, self.y1,
                                             self.x2, self.y2,
                                             self.x3, self.y3,
                                             self.x4, self.y4,
                                             fill="red")


def everything():
    root = Tk()
    root.title("Obdlzniky")
    root.resizable(False, False)

    canvas = tk.Canvas(root,
                       width=500,
                       height=500,
                       borderwidth=2,
                       relief="solid")
    canvas.grid()

    txt = open('../ZADANIA/VYBER_3/Zadanie_6_Uloha_1.txt', 'r').readlines()

    for x in txt:
        temporary = x.split(' ')
        temporary = list(map(int, temporary))

        x1 = temporary[0]
        x2 = temporary[2]
        y1 = temporary[1]
        y2 = temporary[3]

        rec = Rectangle(canvas, x1, y1, x2, y2)
        print(rec)
    root.mainloop()


def just_one():
    number = int(input('set number of Rectangle: '))

    root = Tk()
    root.title("Obdlznik")
    root.resizable(False, False)

    canvas = tk.Canvas(root,
                       width=500,
                       height=500,
                       borderwidth=2,
                       relief="solid")
    canvas.grid()

    txt = open('../ZADANIA/Zadanie_6_Uloha_1.txt', 'r').readlines()

    temporary = txt[number].split(' ')
    temporary = list(map(int, temporary))

    x1 = temporary[0]
    x2 = temporary[2]
    y1 = temporary[1]
    y2 = temporary[3]

    rec1 = Polygon(canvas, x1, y1, x2, y2, 0)
    rec2 = Polygon(canvas, x1, y1 + 200, x2, y2 + 200, 45)
    print(rec1, rec2)
    root.mainloop()


what_to_do = input('1 or all: ')
if what_to_do == '1':
    just_one()

elif what_to_do == 'all':
    everything()
