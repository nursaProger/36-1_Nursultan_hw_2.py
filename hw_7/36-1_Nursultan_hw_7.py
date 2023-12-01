import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    product_title TEXT NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
''')

def add_products():
    products = [
        ('Мыло детское', 50.0, 10),
        ('Шапмунь для волос', 120.0, 5),
        ('Зубная паста', 80.0, 8),
        ('Зубная щетка', 40.0, 12),
        ('Гель для душа', 150.0, 6),
        ('Дезодорант', 100.0, 7),
        ('Бальзам для губ', 60.0, 9),
        ('Крем для рук', 90.0, 11),
        ('Крем для лица', 200.0, 4),
        ('Туалетная бумага', 30.0, 15),
        ('Бумажные салфетки', 20.0, 20),
        ('Мыло жидкое', 70.0, 10),
        ('Скраб для тела', 180.0, 3),
        ('Маска для волос', 160.0, 5),
        ('Лосьон для тела', 170.0, 6)
    ]
    cursor.executemany('''
    INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)
    ''', products)
    conn.commit()


def update_quantity(id, new_quantity):
    cursor.execute('''
    UPDATE products SET quantity = ? WHERE id = ?
    ''', (new_quantity, id))
    conn.commit()


def update_price(id, new_price):
    cursor.execute('''
    UPDATE products SET price = ? WHERE id = ?
    ''', (new_price, id))
    conn.commit()


def delete_product(id):
    cursor.execute('''
    DELETE FROM products WHERE id = ?
    ''', (id,))
    conn.commit()


def select_all_products():
    cursor.execute('''
    SELECT * FROM products
    ''')
    products = cursor.fetchall()
    print('Все товары:')
    for product in products:
        print(product)


def select_cheap_and_many_products(price_limit, quantity_limit):
    cursor.execute('''
    SELECT * FROM products WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    products = cursor.fetchall()
    print(f'Товары, которые дешевле {price_limit} сом и количество которых больше {quantity_limit} шт: ')
    for product in products:
        print(product)



add_products()
select_all_products()
update_quantity(1, 20)
update_price(2, 140.0)
delete_product(3)
select_all_products()
select_cheap_and_many_products(100, 5)

conn.close()