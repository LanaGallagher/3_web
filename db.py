import sqlite3 as sql 

def connection(path):
    connect = sql.connect(path)
    cursor = connect.cursor()
    return connect, cursor

def commit(con):
    con.commit()
    con.close()

# создание баз данных
def create_db(path):
    connect, cursor = connection(path)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            pwd TEXT,
            salt TEXT,
            num_char INTEGER,
            result TEXT
        );
        """
    )
    commit(connect)


# запись баз данных
def write_db(path, data):
    connect, cursor = connection(path)
    cursor.executemany(
        "INSERT INTO data (pwd, salt, num_char, result) VALUES (?,?,?,?);",
        data 
    )
    commit(connect)

# чтение тз БД
def read_db(path):
    connect, cursor = connection(path)
    cursor.execute("SELECT * FROM data;")
    result = cursor.fetchall()
    connect.close()
    return result