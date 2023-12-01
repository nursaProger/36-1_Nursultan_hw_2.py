import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE countries (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL
    )
''')

cursor.execute('''
    INSERT INTO countries (title) VALUES
    ('Кыргызстан'), ('Германия'), ('Китай')
''')

cursor.execute('''
    CREATE TABLE cities (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries (id)
    ) 
''')

cursor.execute('''
    INSERT INTO cities (title, area, country_id) VALUES
    ('Бишкек', 169.6, 1),
    ('Ош', 182.2, 1),
    ('Берлин', 891.8, 2),
    ('Мюнхен', 310.4, 2),
    ('Пекин', 16410.5, 3),
    ('Шанхай', 6340.5, 3),
    ('Гуанчжоу', 7434.4, 3)
''')

cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities (id)
    )
""")

cursor.execute("""
    INSERT INTO students (first_name, last_name, city_id) VALUES
    ('Айдана', 'Сатыбалдиева', 1),
    ('Азамат', 'Токтобеков', 1),
    ('Бекназар', 'Курманбеков', 1),
    ('Динара', 'Жумабаева', 2),
    ('Эльмира', 'Исмаилова', 2),
    ('Фархат', 'Абдуллаев', 2),
    ('Леон', 'Шмидт', 3),
    ('Ханна', 'Мюллер', 3),
    ('Макс', 'Вебер', 3),
    ('Лукас', 'Хоффман', 4),
    ('Лена', 'Шнайдер', 4),
    ('София', 'Краус', 4),
    ('Ли', 'Вэй', 5),
    ('Чэнь', 'Юй', 5),
    ('Ван', 'Цзы', 5)
""")

print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

cursor.execute("SELECT id, title FROM cities")
cities = cursor.fetchall()

for city in cities:
    print(f"{city[0]}. {city[1]}")

while True:
    city_id = input("Введите id города: ")

    if city_id == "0":
        break
    else:
        cursor.execute("""
            SELECT s.first_name, s.last_name, c.title, co.title, c.area
            FROM students s
            JOIN cities c ON s.city_id = c.id
            JOIN countries co ON c.country_id = co.id
            WHERE s.city_id = ?
        """, (city_id,))

        students = cursor.fetchall()

        if students:
            print("Список учеников:")
            for student in students:
                print(
                    f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[3]}, Город: {student[2]}, Площадь города: {student[4]}")
        else:
            print("Нет учеников в этом городе.")

conn.close()