from django.urls import path

from applications.books.views import HomePageView, ListingBooksView, AddBookView, DetailBookView, DeleteBookView, \
    AddAuthorView, AddGenreView

app_name = 'books'


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path(r'listing/', ListingBooksView.as_view(), name='listing'),
    path(r'book/add/', AddBookView.as_view(), name='book-adding'),
    path(r'<int:pk>/', DetailBookView.as_view(), name='details'),
    path(r'delete/<int:pk>/', DeleteBookView.as_view(), name='delete'),
    path(r'author/add/', AddAuthorView.as_view(), name='author-adding'),
    path(r'genre/add/', AddGenreView.as_view(), name='genre-adding'),
]
