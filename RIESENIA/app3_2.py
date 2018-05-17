txt = open('../ZADANIA/VYBER_3/Zadanie_2_Uloha_1.txt', 'r').readlines()
code = open('../ZADANIA/VYBER_3/Zadanie_2_Maska_1.txt', 'r').readlines()

txt_list = []
final_list = []
code_list = []

for x in code:
    hlp = [int(y) for y in x.split()]
    code_list.append(hlp)

for x in txt:
    print(x)
    txt_list.append(x)

counter = 0
for x in code_list:
    for y in x:
        txt_list[counter] = (
            txt_list[counter][:y - 1] + " " + txt_list[counter][y - 1:])
    counter += 1

for x in txt_list:
    print(x)
