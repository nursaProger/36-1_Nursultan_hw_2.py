class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Full_name: {self.full_name}")
        print(f"Age: {self.age}")
        print(f"Marital status: {'Married' if self.is_married else 'Single'}")


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def calc_average_mark(self):
        total_marks = sum(self.marks.values())
        return round(total_marks / len(self.marks), 2)

class Teacher(Person):
    base_salary = 40000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        standart_salary = self.base_salary
        if self.experience > 3:
            bonus_percentage = (self.experience - 3) * 5
            bouns_amount = (bonus_percentage / 100) * standart_salary
            return standart_salary + bouns_amount
        else:
            return standart_salary

teacher = Teacher("Mr.Lucas", 34, 'True', 8)
teacher.introduce_myself()
print(f"Salary: {teacher.calculate_salary()} som\n")


def create_students():
    students = []
    students_1 = Student("Nursultan Keneshbekov", 17, False, {"Math": 90, "Science": 60, "History": 79})
    students_2 = Student("Maksat Aliev", 16, False,{"Math": 45, "Science": 96, "History": 34})
    students_3 = Student("Koralina Anderson", 18, False,{"Math": 95, "Science": 96, "History": 89})
    students.extend([students_1, students_2, students_3])
    return students


students = create_students()

for student in students:
    student.introduce_myself()
    print(f"Average mark: {student.calc_average_mark()}\n")




















































