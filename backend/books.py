from flask import abort
import uuid

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

def read_all():
    return BOOKS

def read_one(id):
    book = [book for book in BOOKS if book['id'] == id]
    if book:
        return book[0]
    else:
        abort(404, f'Book with id {id} not found')