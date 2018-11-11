from django.urls import path

from applications.books.views import HomePageView, ListingBooksView, AddBookView

app_name = 'books'
# app_name = 'authentication'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path(r'listing/', ListingBooksView.as_view(), name='listing'),
    path(r'add/', AddBookView.as_view(), name='adding'),
]
