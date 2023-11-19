
# file = open('new file.txt', 'w', encoding='UTF-8')
# file.write('Какая-то информация! (писать на кириллице)')
# file.close()

# with open('new file.txt', 'a', encoding='UTF-8') as file:
#     file.write('second string #2 (vtoraya stroka)')


# with open('new_file2.txt', 'x') as file:
#     file.write('new data!')


# with open('new_file2.txt', 'r' ) as file:
#     print(file.read())


students = [5, 16, 11, 13, 1, 6, 19, 15, 4, 20, 12, 9]

with open('../HomeWorkGeeks_1/results.txt', 'x') as new_file:
    new_file.write("results test 1 group 31-1\n\n".upper())

while students:
    name = input(f'Введите имя студента под номером {students[0]}')
    rate = input(f'Введите оценку {name}:')
with open
