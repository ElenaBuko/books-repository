from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from applications.books.models import Book


class HomePageView(TemplateView):
    template_name = 'home.html'


class ListingBooksView(ListView):
    model = Book
    template_name = 'listing_books.html'
