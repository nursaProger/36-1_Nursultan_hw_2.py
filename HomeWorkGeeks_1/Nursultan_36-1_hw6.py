#Функция четное-нечетное
def even_odd(number):
    if not isinstance(number, int):
        return None
    if number % 2 == 0:
        return True
    else:
        return False

num1 = 10
result1 = even_odd(num1)
print(result1)

num2 = 7
result2 = even_odd(num2)
print(result2)

num3 = 1.6
result3 = even_odd(num3)
print(result3)



#Функция правописание
def speelling(proposal):
    if proposal[0].isupper() and proposal[-1] == '.':
        return True
    else:
        return False

print(speelling('Эта строка начинается с заглавной буквы и заканчивается точкой.'))
print(speelling('эта строка начинается не с заглавной буквы и не заканчивается точкой'))






#Функция калькулятор
def calc(num1, oper, num2):

    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '*':
        result = num1 * num2
    elif oper == '/':
        if num2 == 0:
            return 'деление на ноль невозможно'
        result = num1 / num2
    elif oper == '%':
        result = num1 % num2
    elif oper == '**':
        result = num1 ** num2
    else:
        return 'неподдерживаемый оператор'

    return result

result1 = calc(2, '**', 3)
print(result1)

result2 = calc(5, '+', 9.6)
print(result2)

result3 = calc(20, '%', 3)
print(result3)

result4 = calc(10, '/', 0)
print(result4)


#Функция "ближайшее число"
def closest_number(sequence, target=0):
    if not sequence:
        return None

    def a_difference(x):
        return abs(x - target)

    closest = min(sequence, key=a_difference)
    return closest

list1 = [5, 20.18, 103, 4]
target1 = 27
result1 = closest_number(list1, target1)
print(result1)

tuple1 = (312, 996, 31, 1991)
target2 = 1000
result2 = closest_number(tuple1, target2)
print(result2)
