import sqlite3
import uuid

connection = sqlite3.connect('books.db')
connection.execute('DROP TABLE IF EXISTS books')

columns = [
    'id TEXT PRIMARY KEY',
    'title TEXT NOT NULL',
    'author TEXT NOT NULL',
    'read BOOLEAN NOT NULL'
]

create_table_cmd = f'CREATE TABLE books ({", ".join(columns)})'
connection.execute(create_table_cmd)

books = [
    (uuid.uuid4().hex, 'On the Road', 'Jack Kerouac', True),
    (uuid.uuid4().hex, 'Harry Potter and the Philosopher\'s Stone', 'J. K. Rowling', False),
    (uuid.uuid4().hex, 'Green Eggs and Ham', 'Dr. Seuss', True)
]

for book in books:
    insert_cmd = f'INSERT INTO books VALUES ("{book[0]}", "{book[1]}", "{book[2]}", {book[3]})'
    connection.execute(insert_cmd)

connection.commit()
connection.close()