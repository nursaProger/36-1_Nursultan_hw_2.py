def count_word(request):

    while True:

        text = (input("введите текст для подсчета слов: "))
        count = text.count(" ") + 1
        print(f'в этом тексте {count} cлов(a)')
        if text == 'stop':
            print("пока...")
            break

    #Калькулятор в функции
    num1 = int(input("enter num1: "))
    oper = input("enter oper: ")
    num2 = int(input("enter num2: "))

    if oper == '+':
        print(f"Ответ: {num1 + num2} :)")
    else:
        print("error")


count_word(0)


