from tkinter import *
import tkinter as tk


class Text:
    def __init__(self, canvas, txt):
        self.canvas = canvas
        self.text = canvas.create_text(-30, 10, text=txt)

    def move(self, counter):
        counter += 1
        print(counter)
        if counter > 300:
            self.canvas.move(self.text, -counter - 30, 0)
            counter = -30
            self.canvas.after(10, self.move, counter)
        else:
            self.canvas.move(self.text, 1, 0)
            self.canvas.after(10, self.move, counter)


txt = input('aky text sa bude premietat: ')

root = Tk()
root.title("Screen saver")
root.resizable(False, False)

canvas = tk.Canvas(root, width=300, height=300, borderwidth=2, relief="solid")
canvas.grid()

counter = -30

my_text = Text(canvas, txt)
my_text.move(counter)

root.mainloop()
