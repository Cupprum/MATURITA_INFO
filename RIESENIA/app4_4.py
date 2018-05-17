txt = open("../ZADANIA/VYBER_4/Zadanie_4_Uloha_1.txt", "r").readlines()

list_moznosti = []

for x in txt:
    list_moznosti.append(x[:-1])

counter_2_ako_0 = 0

for z in range(len(list_moznosti)):
    akt_moznost = list_moznosti[z]
    counter_1 = 0
    counter_2 = 0

    for x in range(0, 6, 2):
        hrac_1 = akt_moznost[x]
        hrac_2 = akt_moznost[x + 1]

        if hrac_1 == hrac_2:
            pass

        kpn = ["k", "p", "n"]
        for y in range(3):
            if hrac_1 == kpn[0]:
                if hrac_2 == kpn[1]:
                    counter_2 += 1

                if hrac_2 == kpn[2]:
                    counter_1 += 1

            kpn = kpn[-1:] + kpn[:-1]

    if counter_2 >= 1:
        counter_2_ako_0 += 1
        print(f"pozicia: {z + 1}")
        print(f"aktualna moznost: {akt_moznost}")
        print(f"body 1. hraca: {counter_1}")
        print(f"body 2. hraca: {counter_2}")

print(f"hrac 2 mal viac ako 1 bod {counter_2_ako_0} krat")
