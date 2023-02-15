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

# Read all books
def read_all():
    return BOOKS

# Read one book
def read_one(id):
    book = [book for book in BOOKS if book['id'] == id]
    if book:
        return book[0]
    else:
        abort(404, f'Book with id {id} not found')

# Create a book
def create(book):
    title = book.get('title')

    if title and title not in [book['title'] for book in BOOKS]:
        book['id'] = uuid.uuid4().hex
        BOOKS.append(book)
        return book, 201
    else:
        abort(409, f'Book with title {title} already exists')

# Update a book
def update(id, book):
    book_to_update = [book for book in BOOKS if book['id'] == id]
    if book_to_update:
        book_to_update[0]['title'] = book.get('title')
        book_to_update[0]['author'] = book.get('author')
        book_to_update[0]['read'] = book.get('read')
        return book_to_update[0]
    else:
        abort(404, f'Book with id {id} not found')