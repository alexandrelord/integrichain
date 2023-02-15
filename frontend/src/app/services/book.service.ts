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

  getBook(id: string): Observable<Book> {
    return this.http.get<Book>(`${API_URL}/${id}`);
  }

  addBook(addBookRequest: Book): Observable<Book> {
    return this.http.post<Book>(API_URL, addBookRequest);
  }

  updateBook(id: string, updateBookRequest: Book): Observable<Book> {
    return this.http.put<Book>(`${API_URL}/${id}`, updateBookRequest);
  }

  deleteBook(id: string): Observable<Book> {
    return this.http.delete<Book>(`${API_URL}/${id}`);
  }
}
