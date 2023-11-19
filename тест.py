class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return (f'Name: {self.__name}\n'
                f'Age: {self.__age}')

if __name__ == '__main__':
    person = Person("Nursultan", 17)
    print(person)


def calculator(num1, num2):
    return num1 + num2

