import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Book } from 'src/app/models/book.models';
import { BookService } from 'src/app/services/book.service';

@Component({
  selector: 'app-add-book',
  templateUrl: './add-book.component.html',
  styleUrls: ['./add-book.component.css']
})
export class AddBookComponent implements OnInit {

  addBookRequest: Book = {
    id: '',
    title: '',
    author: '',
    read: false
  };

  constructor(private bookService: BookService, private router: Router) { }

  ngOnInit(): void {
  }

  addBook() {
    this.bookService.addBook(this.addBookRequest).subscribe({
       next: (book) => {
         this.router.navigate(['/']);
       },
       error: (response) => {
         console.log(response);
       }
    }) 
 }


}
