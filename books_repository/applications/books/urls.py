from django.urls import path

from applications.books.views import HomePageView

app_name = 'books'
# app_name = 'authentication'

urlpatterns = [
   path('', HomePageView.as_view(), name='home')
]