txt = open('../ZADANIA/Zadanie_1_Uloha_1.txt', 'r').readlines()
list_possibilities = []

for x in range(len(txt)):
    help_str = ""
    for y in txt[x][:-1]:
        if y is not " ":
            help_str += y

    list_possibilities.append(help_str)

final_list = []

for x in list_possibilities:
    lenght = len(x)

    counter = 0

    if lenght % 2 == 1:
        for y in range(int(lenght / 2) + 1):
            if x[y].lower() != x[lenght - 1 - y].lower():
                break
            counter += 1
        if counter == int(lenght / 2) + 1:
            final_list.append('ano')
        else:
            final_list.append('nie')

    else:
        for y in range(int(lenght / 2)):
            if x[y].lower() != x[lenght - 1 - y].lower():
                break
            counter += 1
        if counter == int(lenght / 2):
            final_list.append('ano')
        else:
            final_list.append('nie')

for x in range(len(list_possibilities)):
    print(f"{final_list[x]}, {txt[x]}")
