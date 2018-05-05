txt = open('../ZADANIA/Zadanie_3_Uloha_1.txt', 'r').readlines()

day_list = []
other_list = []

for x in range(0, len(txt), 2):
    day_list.append(txt[x][:-1])
    other_list.append(txt[x + 1][:-1])

for x in range(len(day_list)):
    counterBB = 0
    counterBZ = 0
    counterZB = 0
    counterZZ = 0

    for y in range(int(day_list[x]) - 1):
        akt = other_list[x]
        if akt[y] == 'B' and akt[y + 1] == 'B':
            counterBB += 1
        if akt[y] == 'B' and akt[y + 1] == 'Z':
            counterBZ += 1
        if akt[y] == 'Z' and akt[y + 1] == 'B':
            counterZB += 1
        if akt[y] == 'Z' and akt[y + 1] == 'Z':
            counterZZ += 1
    print(f"BB {counterBB}")
    print(f"BZ {counterBZ}")
    print(f"ZB {counterZB}")
    print(f"ZZ {counterZZ}")
    print('\n')
