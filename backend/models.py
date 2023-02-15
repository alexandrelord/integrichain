from config import db, ma

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    read = db.Column(db.Boolean, nullable=False)

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session

book_schema = BookSchema()
books_schema = BookSchema(many=True)