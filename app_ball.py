from tkinter import *


class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2,
                                       self.y2, fill="red")

    def move_down(self):
        self.canvas.move(self.ball, 0, 10)
        self.canvas.after(50, self.move_up)

    def move_up(self):
        self.canvas.move(self.ball, 0, -10)
        self.canvas.after(50, self.move_down)


root = Tk()
root.title("Balls")
root.resizable(False, False)

canvas = Canvas(root, width=300, height=300)
canvas.pack()

ball1 = Ball(canvas, 140, 100, 150, 110)
ball1.move_down()

root.mainloop()
