povodny_text = open("uloha_1.txt", "r")
sifra = open("maska_1.txt", "r")
riesenie = open("riesenie.txt", "w")

list_povodny_text = []
list_sifra = []

for x in povodny_text:
    list_povodny_text.append(x)

for x in sifra:
    list_sifra.append(int(x[:1]))

for x in list_sifra:
    riesenie.write(list_povodny_text[x - 1])

riesenie.close()
