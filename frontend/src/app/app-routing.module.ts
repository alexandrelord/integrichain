import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BooksComponent } from './components/books/books.component';
import { AddBookComponent } from './components/add-book/add-book.component';
import { UpdateBookComponent } from './components/update-book/update-book.component';

const routes: Routes = [
  {
    path: '',
    component: BooksComponent
  },
  {
    path: 'books/add',
    component: AddBookComponent
  },
  {
    path: 'books/update/:id',
    component: UpdateBookComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
