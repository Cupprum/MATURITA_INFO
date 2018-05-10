from PIL import Image
import numpy as np
import webbrowser

webbrowser.open('uloha_3.bmp')

im = Image.open("uloha_3.bmp")
im.rotate(-90)

txt = open('riesenie_uloha3.txt', 'w')

p = np.array(im)
print(f"x: {len(p)}, y: {len(p[0])}")
txt.write(f"x: {len(p)}, y: {len(p[0])}")
txt.write("\n")

for x in p:
    list_docastny = ""
    for y in x:
        if str(y) == "[255 255 255]":
            list_docastny += 'c'
        else:
            list_docastny += 'b'
    txt.write(str(list_docastny))
    txt.write('\n')
