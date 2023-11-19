#генератор сложных паролей
import random
from count_word_text import count_word

chars = 'FCRTBOL,DJEOL,sjokmfpw;x[;l,mgfuhnfc<>/?{}:'
number = input("сколько паролей?: ")
lenght = input("длина паролей: ")
number = int(number)
lenght = int(lenght)
for n in range(number):
    password = ''
    for i in range(lenght):
        password += random.choice(chars)
print(password)

count_word(0)

