from flask import abort, make_response, jsonify
import uuid
from config import db
from models import Book, book_schema, books_schema

# Read all books
def read_all():
    # Use the model to query the database
    books = Book.query.all()
    # Serialize the data for the response
    return books_schema.dump(books)

# Read one book
def read_one(id):
    book = Book.query.get(id)
    
    if book is None:
        abort(404, f'Book with id {id} not found')
    else:
        return book_schema.dump(book)

# Create a book
def create(book):
    title = book.get('title')

    existing_book = Book.query.filter(Book.title == title).one_or_none()

    if existing_book is None:
        new_book = Book(
            id=uuid.uuid4().hex,
            title=title,
            author=book.get('author'),
            read=book.get('read')
        )
        db.session.add(new_book)
        db.session.commit()
        return book_schema.dump(new_book)
    else:
        abort(409, f'Book with title {title} already exists')

# Update a book
def update(id, book):
    update_book = Book.query.get(id)

    if update_book is None:
        abort(404, f'Book with id {id} not found')
    else:
        update_book.title = book.get('title')
        update_book.author = book.get('author')
        update_book.read = book.get('read')
        db.session.commit()
        return book_schema.dump(update_book)

# Delete a book
def delete(id):
    book = Book.query.get(id)

    if book is None:
        abort(404, f'Book with id {id} not found')
    else:
        db.session.delete(book)
        db.session.commit()
        return make_response(jsonify({'message': f'Book {id} deleted'}), 200)
