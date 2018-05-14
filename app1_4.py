# sequence = input('vvjjsskK')
sequence = 'vvjjsskK'
list_final = []

'''
for x in range(int(len(sequence) / 2)):
    print(sequence[x], ' ', sequence[-1 - x])
'''

list_of_letters = list(sequence)
print(list_of_letters)

counter = len(list_of_letters)

for _ in range(counter):
    str_final = list_of_letters[0]

    for _ in range(counter - 1):
        str_final += list_of_letters[1]

        for _ in range(counter - 2):
            str_final += list_of_letters[2]

            for _ in range(counter - 3):
                str_final += list_of_letters[3]

                for _ in range(counter - 4):
                    str_final += list_of_letters[4]

                    for _ in range(counter - 5):
                        str_final += list_of_letters[5]

                        for _ in range(counter - 6):
                            str_final += list_of_letters[6]

                            for _ in range(counter - 7):
                                str_final += list_of_letters[7]

                                if str_final not in list_final:
                                    list_final.append(str_final)
                                str_final = str_final[:-1]

                            str_final = str_final[:-1]
                            list_of_letters.append(list_of_letters[6])
                            del list_of_letters[6]

                        str_final = str_final[:-1]
                        list_of_letters.append(list_of_letters[5])
                        del list_of_letters[5]

                    str_final = str_final[:-1]
                    list_of_letters.append(list_of_letters[4])
                    del list_of_letters[4]

                str_final = str_final[:-1]
                list_of_letters.append(list_of_letters[3])
                del list_of_letters[3]

            str_final = str_final[:-1]
            list_of_letters.append(list_of_letters[2])
            del list_of_letters[2]

        str_final = str_final[:-1]
        list_of_letters.append(list_of_letters[1])
        del list_of_letters[1]

    list_of_letters.append(list_of_letters[0])
    del list_of_letters[0]

print(len(list_final))
