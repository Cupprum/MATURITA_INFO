def algoritmus(a, b):
    while b != 0:
        c = b
        b = a % b
        a = c
    return a


print(algoritmus(24, 20))
