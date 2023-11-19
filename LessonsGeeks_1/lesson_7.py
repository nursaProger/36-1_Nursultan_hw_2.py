# def up_letter(word: str):
#     return word.title()
#
# def show_words(func, list_words):
#     for i in list_words:
#         print(func(i))

# lambda_func = lambda num1, num2: num1 + num2
#
# print(lambda_func(2, 3))
# print(type(lambda_func))
#
# def lamda_func(num1, num2):
#     return num1 + num2
#
# print(lambda_func(2, 3))

# numbers = list(range(1, 16))
# print(numbers)

# filtred_nums = list(filter(lambda num: num > 10, numbers))
# print(filtred_nums)

# mapped_nums = tuple(map(lambda num: num + 5, numbers))
# print(mapped_nums)
def nearest_num(numbers, target):
    return max(numbers, key=lambda num: abs(target-num))

print(nearest_num([111, 99, 15, 20], target=100))


