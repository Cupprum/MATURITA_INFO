import time


def hex_to_dec(num):
    numbers1_9 = range(0, 10)
    numbers1_9 = [str(x) for x in numbers1_9]

    numbers10_15 = ['a', 'b', 'c', 'd', 'e', 'f']

    if num in numbers1_9:
        return(int(num))

    elif num in numbers10_15:
        position = numbers10_15.index(num)
        return(10 + position)


txt = open('../ZADANIA/VYBER_1/uloha_5.txt').readlines()

list_groups = []

for x in txt:
    list_groups.append(x[:-1])

start_time = time.time()

for x in list_groups:
    list_hex = list(x)
    list_dec = []

    for y in list_hex:
        list_dec.append(hex_to_dec(y))
    list_dec_sorted = list_dec[:]
    list_dec_sorted.sort()

    if list_dec == list_dec_sorted:
        print(f"vporiadku {list_hex}")
        pass

print(f"moj {(time.time() - start_time)}")

start_time = time.time()

for x in list_groups:
    list_hex = list(x)
    list_dec = []

    for y in list_hex:
        list_dec.append(hex_to_dec(y))

    counter = 0
    help_var = -1
    bezkaj = True

    while bezkaj:
        if counter == len(list_dec):
            print(f"vporiadku {list_hex}")
            break

        actual_number = list_dec[counter]

        if actual_number > help_var:
            help_var = actual_number
            counter += 1
        else:
            bezkaj = False

print(f"otcov {(time.time() - start_time)}")
