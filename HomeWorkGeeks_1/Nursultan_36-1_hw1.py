
exp_1 = int(input("Введите расход за понедельник: "))
exp_2 = int(input("Введите расход за вторник: "))
exp_3 = int(input("Введите расход за среду: "))
exp_4 = int(input("Введите расход за четверг: "))
exp_5 = int(input("Введите расход за пятницу: "))
exp_6 = int(input("Введите расход за субботу: "))
exp_7 = int(input("Введите расход за воскресенье: "))


amount = exp_1 + exp_2 + exp_3 + exp_4 + exp_5 + exp_6 + exp_7
print(f"Общая сумма расхода за неделю составляет: {amount}")


average_cpd = amount / 7
print("Ваш средний расход в день составляет: ", round(average_cpd, 1))


if amount > 20000:
    print("потрачено много")
elif amount > 10000 < 20000:
    print("потрачено средне")
elif amount > 0 < 10000:
    print("потрачено мало")
else:
    print("не потрачено ничего")








# temperature = int(input('inter temperature: '))
#
# if temperature >= -50 and temperature <= 0:
#     print('cold')
# elif temperature >= 1 and temperature <= 10:
#     print('cool')
# elif temperature >= 11 and temperature <= 25:
#     print('warm')
# elif temperature >= 26 and temperature <= 50:
#     print('heat')
# else:
#     print('ты умрешь! не выходи! смертЪ')


