from django.urls import path

from applications.books.views import HomePageView

app_name='books'

urlpatterns = [
   path('', HomePageView.as_view(), name='index')
]