# система управления базами данных (СУБД) SQLite

import sqlite3 as sql

# соединение с базой данных (БД)
conn = sql.connect("test.db")

# курсор - "панель управления БД"
cur = conn.cursor()

# создание таблицы
sql_cmd = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRYMARY KEY,
    f_name TEXT,
    l_name TEXT,
    age REAL,
    gender TEXT
);
"""
cur.execute(sql_cmd)
conn.commit()

# запись данных
# одна строка
# sql_cmd = "INSERT INTO users VALUES (?,?,?,?,?);"
# cur.execute(sql_cmd, (0, "Gendalf", "Gray", 452.3, "m"))
# conn.commit()

# много строк
# sql_cmd = "INSERT INTO users VALUES (?,?,?,?,?);"
# my_users = [
#     (1, "Harry", "Potter", 23.5, "m"),
#     (2, "Mary", "Jane", 23.0, "f"),
#     (3, "Tom", "Riddle", 56.4, "m")
# ]
# cur.executemany(sql_cmd, my_users)
# conn.commit()


# чтение данных из БД
# sql_cmd = "SELECT * FROM users;"
# cur.execute(sql_cmd)

# # все строки
# # result = cur.fetchall()
# # result = cur.fetchmany(2)

# # первая строка
# result = cur.fetchone()
# print(result)

# # чтение данных из определенных столбцов в БД
# sql_cmd = "SELECT user_id, f_name, age FROM users;"
# cur.execute(sql_cmd)
# result = cur.fetchall()
# print(result)

# чтение данных из определенных столбцов с условием (фильтр)
# sql_cmd = "SELECT user_id, f_name, age FROM users WHERE age < 30;"
# sql_cmd = "SELECT user_id, f_name, age FROM users WHERE age < 30 AND gender = 'f';"
# cur.execute(sql_cmd)
# result = cur.fetchall()
# print(result)

# удаление данных из БД
# sql_cmd = "DELETE FROM users WHERE l_name = 'Potter';"
# cur.execute(sql_cmd)
# conn.commit()

# создание второй таблицы
sql_cmd = """
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRYMARY KEY,
    date TEXT,
    user_id INTEGER,
    total REAL
);
"""
cur.execute(sql_cmd)
conn.commit()

# запись данных во вторую таблицу
# sql_cmd = "INSERT INTO orders VALUES (?,?,?,?);"
# orders = [
#     (0, "02-09-2023", 2, 2500),
#     (1, "15-10-2023", 1, 569.50),
#     (2, "01-11-2023", 2, 956.3),
#     (3, "02-11-2023", 4, 666,6)
# ]
# cur.executemany(sql_cmd, orders)
# conn.commit()


# чтение данных из двух таблиц
# sql_cmd = "SELECT * FROM users LEFT JOIN orders ON users.user_id = orders.user_id;"
sql_cmd = "SELECT * FROM users INNER JOIN orders ON users.user_id = orders.user_id;"
cur.execute(sql_cmd)
result = cur.fetchall()
print(result)

# закрытие соединения
conn.close()