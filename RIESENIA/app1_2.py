import random
import tkinter as tk
from tkinter import *


root = tk.Tk()
canvas = tk.Canvas(root,
                   width=400,
                   height=600,
                   borderwidth=0,
                   highlightthickness=0,
                   bg="black")
canvas.grid()


def potvrdenie():
    list_random_cisel = []
    pocet = input_loop.get()
    print(f"pocet {pocet}")

    for x in range(int(pocet)):
        random_value = random.randint(1, 6)
        print(random_value)
        list_random_cisel.append(random_value)

    vypocet(list_random_cisel)


def vypocet(list_random_cisel):
    for iterator_aktual in list_random_cisel:
        root.after(1000, update_text(iterator_aktual))


def update_text(iterator_aktual):
    text_list = ["text_1",
                 "text_2",
                 "text_3",
                 "text_4",
                 "text_5",
                 "text_6"]

    text_list2 = [text_1,
                  text_2,
                  text_3,
                  text_4,
                  text_5,
                  text_6]

    canvas.itemconfigure(text_aktualne, text=iterator_aktual)
    for x in range(0, len(text_list)):
        if int(iterator_aktual) == int(text_list[x][5:]):
            print(iterator_aktual)
            canvas.insert(text_list2[x], tk.END, "*")
            canvas.update()


def _kruh(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


def _text(self, x, y, **kwargs):
    return self.create_text(x, y, **kwargs)


tk.Canvas.kruh = _kruh
tk.Canvas.text = _text

kruh = canvas.kruh(200, 200, 100, fill="#fff", width=0)
text_aktualne = canvas.text(200, 200, text="")
text_1 = canvas.text(200, 410, text="1: ", fill="white")
text_2 = canvas.text(200, 430, text="2: ", fill="white")
text_3 = canvas.text(200, 450, text="3: ", fill="white")
text_4 = canvas.text(200, 470, text="4: ", fill="white")
text_5 = canvas.text(200, 490, text="5: ", fill="white")
text_6 = canvas.text(200, 510, text="6: ", fill="white")

input_loop = Entry(root)
input_loop.grid()
pocet_loopov = canvas.create_window(200, 10, width=100, window=input_loop)

enter_button = Button(root, text="potvrdenie", command=potvrdenie)
enter_button.grid()
tlacitko = canvas.create_window(200, 35, width=100, window=enter_button)

root.mainloop()
