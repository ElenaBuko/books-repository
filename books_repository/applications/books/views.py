from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView

from applications.books.models import Book


class HomePageView(TemplateView):
    template_name = 'home.html'


class ListingBooksView(ListView):
    model = Book
    template_name = 'listing_books.html'


class DetailBookView(DetailView):
    model = Book
    template_name = 'details_book.html'

    def get_absolute_url(self):
        return reverse('books:details', kwargs={'pk': self.id})


class AddBookView(CreateView):
    model = Book
    template_name = 'add_book.html'
    fields = ('name', 'author', 'genre', 'is_read')
    success_url = 'books:listing'

    # def get_success_url(self):
    #     return reverse('books:listing')

    def form_valid(self, form):
        form.save(commit=True)
        return redirect(self.success_url)


# class DeleteBookView(DeleteView):
#     model = Book
#     template_name = 'delete_book.html'
#
#     def get_success_url(self):
#         return reverse('books:listing')
