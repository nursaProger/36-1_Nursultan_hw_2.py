class Figure:
    unit = 'cm'
    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value


    def calculate_area(self):
        raise NotImplementedError('Subclasses should implement this method')

    def calculate_perimeter(self):
        raise NotImplementedError('Subclasses should implement this method')

    def info(self):
        raise NotImplementedError('Subclasses should implement this method')


class Square(Figure):
    def __init__(self, side_lenght):
        super(Square, self).__init__()
        self.__side_lenght = side_lenght
        self.perimeter = self.calculate_perimeter()


    def calculate_area(self):
        return self.__side_lenght * self.__side_lenght


    def calculate_perimeter(self):
        return 4 * self.__side_lenght


    def info(self):
        return f'Square side lenght: {self.__side_lenght}{self.unit}, perimeter: {self.perimeter}{self.unit}, area: {self.calculate_area()}{self.unit}'


class Rectangle(Figure):
    def __init__(self, lenght, width):
        super(Rectangle, self).__init__()
        self.__lenght = lenght
        self.__width = width
        self.perimeter = self.calculate_perimeter()


    def calculate_area(self):
        return self.__lenght * self.__width


    def calculate_perimeter(self):
        return 2 * (self.__lenght + self.__width)


    def info(self):
        return f'Rectangle lenght: {self.__lenght}{self.unit}, width: {self.__width}{self.unit}, perimeter: {self.perimeter}{self.unit}, area: {self.calculate_area()}{self.unit}'


figure_list = [
    Square(5),
    Square(8),
    Rectangle(6, 9),
    Rectangle(3, 5),
    Rectangle(6, 4)
]

for figure in figure_list:
    print(figure.info())






























