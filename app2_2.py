from tkinter import *
import tkinter as tk
import time


class Kruznica:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.make_circle = canvas.create_oval(self.x1, self.y1,
                                              self.x2, self.y2,
                                              fill="blue")


class Lichobeznik:
    def __init__(self, canvas, x1, y1, x2, y2, x3, y3, x4, y4):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.make_trapeze = canvas.create_polygon(self.x1, self.y1,
                                                  self.x2, self.y2,
                                                  self.x3, self.y3,
                                                  self.x4, self.y4,
                                                  fill="green")


class Trojuholnik:
    def __init__(self, canvas, x1, y1, x2, y2, x3, y3):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.make_triangel = canvas.create_polygon(self.x1, self.y1,
                                                   self.x2, self.y2,
                                                   self.x3, self.y3,
                                                   fill="red")


def middle_out():
    circle = Kruznica(canvas, 100, 100, 200, 200)
    root.update_idletasks()

    trapeze = Lichobeznik(canvas, 100, 200, 200, 200, 170, 100, 130, 100)
    time.sleep(1)
    root.update_idletasks()

    triangel = Trojuholnik(canvas, 100, 200, 200, 200, 150, 114)
    time.sleep(1)
    root.update_idletasks()

    print(circle, trapeze, triangel)


def in_row(counter):
    if counter < 800:
        circle = Kruznica(canvas,
                          counter,
                          100,
                          100 + counter,
                          200)
        counter += 100
        print(circle)

    if counter < 800:
        trapeze = Lichobeznik(canvas,
                              counter,
                              200,
                              100 + counter,
                              200,
                              70 + counter,
                              100,
                              30 + counter,
                              100)
        counter += 100
        print(trapeze)

    if counter < 800:
        triangel = Trojuholnik(canvas,
                               counter,
                               200,
                               100 + counter,
                               200,
                               50 + counter,
                               114)
        counter += 100
        print(triangel)

    if counter < 800:
        in_row(counter)


what_to_do = input('stred / postupne : ')

if what_to_do == 'stred':
    root = Tk()
    root.title("Utvary")
    root.resizable(False, False)
    canvas = tk.Canvas(root, width=300, height=300,
                       borderwidth=2, relief="solid")
    canvas.grid()

    middle_out()

elif what_to_do == 'postupne':
    root = Tk()
    root.title("Utvary")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=800, height=300,
                       borderwidth=2, relief="solid")
    canvas.grid()

    counter = 0
    in_row(counter)

else:
    print('incorrect input')

root.mainloop()
