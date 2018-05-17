txt = open('../ZADANIA/VYBER_2/uloha_4.txt', 'r').readlines()
final = open('final2_4.txt', 'w')

list_temporary = []

for x in txt:
    list_temporary.append(x[:-1])

for x in list_temporary:
    help_str = x[:]
    help_str += x[0]
    help_str = help_str[1:]
    final.write(help_str + "\n")
