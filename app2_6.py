import random

list_kodov = []
zakladnykod = "0"
for x in range(6):
    docastny_kod = ""
    for y in zakladnykod:
        if zakladnykod[int(y)] == "0":
            docastny_kod += "01"
        else:
            docastny_kod += "10"
    list_kodov.append(docastny_kod)
    zakladnykod = docastny_kod

position = random.randint(1, 6)
aktualny_kod = list_kodov[position - 1]

print(f"pozicia: {position}")
print(f"dlzka kodu: {len(aktualny_kod)}")
print(f"kod: {aktualny_kod}")

counter = 0
for x in range(len(aktualny_kod) - 1):
    prva = aktualny_kod[x]
    druha = aktualny_kod[x + 1]
    if prva + druha == "01":
        counter += 1
print(f"01 sa nachadza v kode {counter} krat")
