while True:
    num_1 = int(input('введите первое число: '))
    oper = input("введите оператор: ")
    num_2 = int(input('введите второе число: '))

    if oper == '+':
        print('ответ: ', num_1 + num_2)
    elif oper == '-':
        print('ответ: ', num_1 - num_2)
    elif oper == '*':
        print('ответ: ', num_1 * num_2)
    elif oper == '/':
        print('ответ: ', num_1 / num_2)
    else:
        print('вы ввели не допустимый оператор')

    exit = input("чтобы продолжить нажмите любую клавишу, чтобы выйти напишите 'stop': ")
    if exit == 'stop':
        print("пока...")
        break

