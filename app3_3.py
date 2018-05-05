txt = open('../ZADANIA/Zadanie_3_Uloha_1.txt', 'r').readlines()

day_list = []
other_list = []
stat_list = ['BB', 'BZ', 'ZB', 'ZZ']

for x in range(0, len(txt), 2):
    day_list.append(txt[x][:-1])
    other_list.append(txt[x + 1][:-1])

for x in range(len(day_list)):
    dic_counters = {'counterBB': 0,
                    'counterBZ': 0,
                    'counterZB': 0,
                    'counterZZ': 0}

    for y in range(int(day_list[x]) - 1):
        akt = other_list[x]
        for z in stat_list:
            if akt[y] == z[0] and akt[y + 1] == z[1]:
                dic_counters['counter' + z] += 1

    print(dic_counters)
