import sqlite3

CREATE_TABLE = "CREATE TABLE IF NOT EXISTS keyboards (id INTEGER PRIMARY KEY, name TEXT, switch TEXT, brand TEXT, rating INTEGER);"

INSERT_KB = "INSERT INTO keyboards (name, switch, brand, rating) VALUES (?, ?, ?, ?);"

GET_ALL_KB = "SELECT * FROM keyboards"

GET_KB_BY_NAME = "SELECT * FROM keyboards WHERE name = ?;"

GET_BEST_KB = "SELECT * FROM keyboards ORDER BY rating DESC LIMIT 1;"

def connect():
  return sqlite3.connect("data.db")

def create_table(connection):
  with connection:
    connection.execute(CREATE_TABLE)
  
def add_kb(connection, name, switch, brand, rating):
  with connection:
    connection.execute(INSERT_KB, (name, switch, brand, rating,))

def get_all_kb(connection):
  with connection:
    return connection.execute(GET_ALL_KB).fetchall()

def get_kb_by_name(connection, name):
  with connection:
    return connection.execute(GET_KB_BY_NAME, (name,)).fetchall()

def get_best_kb(connection):
  with connection:
    return connection.execute(GET_BEST_KB).fetchone()