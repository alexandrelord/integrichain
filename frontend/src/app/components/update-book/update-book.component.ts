import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Book } from 'src/app/models/book.models';
import { BookService } from 'src/app/services/book.service';

@Component({
  selector: 'app-update-book',
  templateUrl: './update-book.component.html',
  styleUrls: ['./update-book.component.css']
})
export class UpdateBookComponent implements OnInit {

  book: Book = {
    id: '',
    title: '',
    author: '',
    read: false
  };

  constructor(private route: ActivatedRoute, private bookService: BookService, private router: Router) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe({
      next: params => {
        const id = params.get('id');
        if (id) {
          this.getBook(id);
        }
      }
    })
    }

    getBook(id: string): void {
      this.bookService.getBook(id).subscribe({
        next: book => {
          this.book = book;
        },
        error: (response) => {
          console.log(response);
        }
      })
    }

    updateBook(): void {
      this.bookService.updateBook(this.book.id, this.book).subscribe({
        next: book => {
          this.router.navigate(['/']);
        },
        error: (response) => {
          console.log(response);
        }
      })
    }
}
