# sequence = input('vvjjsskK')
sequence = 'vjskKsjv'
print(sequence)
list_final = []

for x in range(int(len(sequence) / 2)):
    print(sequence[x], ' ', sequence[-1 - x])

list_of_letters = list(sequence)
print(list_of_letters)
