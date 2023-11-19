def nearest_number(numbers, target):
    numbers.sort(key=lambda x: abs(x - target))
    return (target, numbers)

result1 = nearest_number([312, 996, 31, 1991], 1000)
print(result1)

result2 = nearest_number([5, 20.18, 103, 4], 27)
print(result2)

def get_element(iterable):
    while True:
        try:
            index = int(input("Введите индекс элемента: "))
            if 0 <= index < len(iterable):
                print("Элемент:", iterable[index])
            else:
                print("Индекс вне допустимого диапазона, попробуйте снова.".format(len(iterable) - 1))
        except ValueError:
            print("Неверный формат индекса. Введите целое число.")



my_list = [10, 20, 30, 40, 50]
get_element(my_list)

#использование filter с lambda для фильтрации четных чисел из списка
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)

#использование map c lambda для умножения каждого элемента списка на 2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)