from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from applications.books.models import Book


class HomePageView(TemplateView):
    template_name = 'home.html'


class ListingBooksView(TemplateView):
    template_name = 'listing_books.html'
