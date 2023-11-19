data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []
for i in data_tuple:
    if isinstance(i, str):
        letters.append(i)
    else:
        numbers.append(i)


numbers.remove(6.13)
letters.append(True)

numbers.insert(-1, 2)
numbers.sort()
letters.reverse()
numbers.remove(1)

letters[1] = 'G'
letters[3] = 'e'

numbers = [x ** 2 for x in numbers]

letters_tuple = tuple(letters)
numbers_tuple = tuple(numbers)


print(letters_tuple)
print(numbers_tuple)






