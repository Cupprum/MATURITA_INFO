txt = open('../ZADANIA/Zadanie_7_Uloha_1.txt', 'r').readlines()

list_square = []
list_actual_numbers = []

for x in range(0, len(txt) - 1, 2):
    list_square.append(txt[x][:-1])
    list_actual_numbers.append(txt[x + 1][:-1])


list_square = list(map(int, list_square))

dic_final = {}
counter = 1

for x in range(len(list_square)):
    temporary1 = list_actual_numbers[x].split(" ")
    temporary1 = list(map(int, temporary1))

    square = list_square[x] * list_square[x]
    list_for_push = []

    for y in range(0, square, list_square[x]):
        temporary2 = []

        for z in range(list_square[x]):
            temporary2.append(temporary1[y + z])

        list_for_push.append(temporary2)

    dic_final.update({'matrix' + str(counter): list_for_push})
    counter += 1

for x in dic_final.values():

    maximum_y = 0
    maximum_y_value = 0

    for y in range(len(x)):
        if max(x[y]) > maximum_y_value:
            maximum_y = y + 1
            maximum_y_value = max(x[y])
        print(x[y])

    counter = 1

    for y in x[maximum_y - 1]:
        if y == maximum_y_value:
            break
        counter += 1

    print(f"stlpec {counter}")
    print(f"riadok {maximum_y}")
    print(f"maximum_y_value {maximum_y_value}")
