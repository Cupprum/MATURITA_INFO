import math

txt = open('../ZADANIA/VYBER_4/Zadanie_7_Uloha_1.txt', 'r').readlines()

list_groups = []
list_animals_in_groups_temporary = []
list_animals_in_groups = []
list_final = []

for x in range(0, len(txt), 2):
    list_groups.append(txt[x][:-1])
    list_animals_in_groups_temporary.append(txt[x + 1][:-1])

list_groups = list(map(int, list_groups))

for x in list_animals_in_groups_temporary:
    temporary = list(map(int, x.split(' ')))
    list_animals_in_groups.append(temporary)

print(list_groups)
print(list_animals_in_groups)

for x in range(len(list_groups)):
    groups_at_least = math.ceil(list_groups[x] / 2)

    actual_sorted = list_animals_in_groups[x]
    actual_sorted.sort()
    actual_sorted = actual_sorted[:groups_at_least]

    lit_min_votes = []

    for y in actual_sorted:
        min_votes = math.ceil(y / 2)
        lit_min_votes.append(min_votes)

    list_final.append(sum(lit_min_votes) + 1)

for x in list_final:
    print(x)
