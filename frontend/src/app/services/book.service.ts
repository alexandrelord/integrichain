import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Book } from '../models/book.models';

const API_URL = 'http://localhost:8000/api/books';

@Injectable({
  providedIn: 'root'
})
export class BookService {

  constructor(private http: HttpClient) { }

  getBooks(): Observable<Book[]> {
    return this.http.get<Book[]>(API_URL);
  }

  addBook(addBookRequest: Book): Observable<Book> {
    return this.http.post<Book>(API_URL, addBookRequest);
  }
}
