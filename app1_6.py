from tkinter import *

root = Tk()


txt = open("uloha_6.txt", "r").readlines()

list_n = []
list_of_nums = []

for x in range(0, len(txt), 2):
    n = int(txt[x][0])
    list_n.append(n)

    temp_list1 = txt[x + 1][:-1].split(" ")
    temp_list2 = []
    for y in temp_list1:
        temp_list2.append(int(y))
    list_of_nums.append(temp_list2)

list_of_matrixes = []

col = 0
for x in range(len(list_n)):
    n = list_n[x]
    list_of_n = list_of_nums[x]

    for y in range(0, len(list_of_n), n):
        str_of_line = ""
        for z in range(n):
            printed_name = str(list_of_n[y + z])
            if int(printed_name) % 2 == 0:
                printed_name = "*"
            nazov_meno = Label(text=printed_name)
            nazov_meno.grid(row=col, column=z, pady=1)
            str_of_line += str(list_of_n[y + z]) + " "
        print(str_of_line)
        col += 1
    print(" ")
    nazov_meno = Label(text=" ")
    nazov_meno.grid(row=col, column=z, pady=1)
    col += 1

mainloop()
