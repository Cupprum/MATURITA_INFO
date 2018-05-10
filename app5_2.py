from tkinter import *
import tkinter as tk


class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2,
                                       self.y2, fill="red")

    def move(self, y, maximum, direction):
        if direction == 'down':
            if y > 0:
                self.canvas.move(self.ball, 0, 1)
                self.canvas.after(5, self.move, y - 1, maximum, 'down')
            elif y == 0:
                self.canvas.after(5, self.move, y, int(maximum * 0.8), 'up')
        elif direction == 'up':
            if y < maximum:
                self.canvas.move(self.ball, 0, -1)
                self.canvas.after(5, self.move, y + 1, maximum, 'up')
            elif y == maximum:
                self.canvas.after(5, self.move, y, maximum, 'down')


def start_the_game():
    parameters = int(set_size_entry.get())

    ball1 = Ball(canvas,
                 150 - int(parameters / 2),
                 300 - parameters,
                 150 + int(parameters / 2),
                 300)
    ball1.move(0, 300 - parameters, 'up')


root = Tk()
root.title("Balls")
root.resizable(False, False)

set_size_entry = tk.Entry(root, width=9)
set_size_entry.grid(row=0, column=0)
set_size_button = tk.Button(root, text='Start', command=start_the_game)
set_size_button.grid(row=0, column=1)

canvas = tk.Canvas(root, width=300, height=300, borderwidth=2, relief="solid")
canvas.grid(row=1, column=0)


root.mainloop()
