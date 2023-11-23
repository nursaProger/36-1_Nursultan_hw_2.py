#Функция сортировки пузырьком
def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n - i -1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

unsorted_list = [12, 4, 6, 56, 9, 1]
sorted_list = bubble_sort(unsorted_list)
print(f"Отсортированный список: {sorted_list}")



#Функция бинарного поиска
def binary_search(A, Val):
    first = 0
    last = len(A)-1
    result = False

    while first < last:
        middle = (first + last) // 2
        if A[middle] == Val:
            result = True
            break
        elif A[middle] < Val:
            first = middle + 1
        else:
            last = middle - 1

    if result:
        return middle
    else:
        return -1

N = 100
Val = 50
num = list(range(N))
result = binary_search(num, Val)

if result != -1:
    print('Элемент найден:', result)
else:
    print('Элемент не найден!')



