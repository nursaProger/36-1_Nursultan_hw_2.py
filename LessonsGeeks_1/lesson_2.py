# time = input('введите время суток: '). lower()
#
# if time == 'утро' or time == 'morning':
#     print("доброе утро")
# elif time == 'день' or time == 'day':
#     print("добрый день")
# elif time =='вечер' or time == 'evening':
#     print("добрый вечер")
# else:
#     print('здравствуйте! (точное время суток неопределено!')


word = 'конфигурация'

age = int(input('enter age: '))

if age >= 18:
    print("welcome")
else:
    print(f'вход запрещен! приходите через {18-age} лет')




# print(word[0:3]
# print(word[0])
# print(word[5])
zod_sign = int(input("Введите день рождения: "))
znak = int(input("Введите месяц рождения:"))


if zod_sign > 20 < 31 and znak == 3:
    print("овен")
elif zod_sign > 0 < 21 and znak == 4:
    print("овен")

if zod_sign > 21 < 31 and znak == 4:
    print("телец")
elif zod_sign > 0 < 21 and znak == 5:
    print("телец")

if zod_sign > 22 < 31 and znak == 5:
    print("близнецы")
elif zod_sign > 0 < 21 and znak == 6:
    print("близнецы")

if zod_sign > 22 < 31 and znak == 6:
    print("рак")
elif zod_sign > 0 < 22 and znak == 7:
    print("рак")

if zod_sign > 23 < 31 and znak == 7:
    print("")
elif zod_sign > 0 < 23 and znak == 8:
    print("")

if zod_sign > 24 < 31 and znak == 4:
    print("")
elif zod_sign > 0 < 24 and znak == 5:
    print("телец")

if zod_sign > 25 < 31 and znak == 4:
    print("телец")
elif zod_sign > 0 < 25 and znak == 5:
    print("телец")

if zod_sign > 26 < 31 and znak == 4:
    print("телец")
elif zod_sign > 0 < 26 and znak == 5:
    print("телец")

if zod_sign > 28 < 31 and znak == 4:
    print("телец")
elif zod_sign > 0 < 28 and znak == 5:
    print("телец")

if zod_sign > 29 < 31 and znak == 4:
    print("телец")
elif zod_sign > 0 < 29 and znak == 5:
    print("телец")

if zod_sign > 30 < 31 and znak == 4:
    print("телец")
elif zod_sign > 0 < 30 and znak == 5:
    print("телец")

if zod_sign > 21 < 31 and znak == 4:
    print("телец")
elif zod_sign > 0 < 21 and znak == 5:
    print("телец")


    if word == 'stop':
        print("пока...")
        break