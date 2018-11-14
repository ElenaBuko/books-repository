from django.urls import path

from applications.books.views import HomePageView, ListingBooksView, AddBookView, DetailBookView, DeleteBookView


app_name = 'books'


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path(r'listing/', ListingBooksView.as_view(), name='listing'),
    path(r'add/', AddBookView.as_view(), name='adding'),
    path(r'<int:pk>/', DetailBookView.as_view(), name='details'),
    path(r'delete/<int:pk>/', DeleteBookView.as_view(), name='delete'),
]
