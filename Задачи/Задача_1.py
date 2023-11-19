num1 = int(input("Enter number one: "))
operations = input("Enter opeator: ")
num2 = int(input("Enter number two: "))

while True:
    if operations == '+':
        print(f'Ответ: {num1 + num2}')
    else:
        print("Error")

    exitt = input("Чтобы выйти напишите 'stop', либо введите что угодно, чтобы продолжить: ")

    if exitt == 'stop':
        print("Exit..")
        break







