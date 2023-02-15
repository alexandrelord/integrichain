import { Component, OnInit } from '@angular/core';
import { Book } from '../../models/book.models';
import { BookService } from '../../services/book.service';

@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css']
})
export class BooksComponent implements OnInit {

  books: Book[] = [];
  
  constructor(private bookService: BookService) {}

  ngOnInit(): void {
    this.getBooks();
  }

  getBooks(): void {
    this.bookService.getBooks().subscribe({
      next: books => {
        this.books = books;
      },
      error: (response) => {
        console.log(response);
      }
    })
  }

  deleteBook(id: string): void {
    this.bookService.deleteBook(id).subscribe({
      next: books => {
        this.getBooks();
      },
      error: (response) => {
        console.log(response);
      }
    })
  }
  
}
