from django.urls import path

from applications.auth.views import LoginView, RegistrationView
from applications.books.views import HomePageView

app_name = 'auth'

urlpatterns = [
   path(r'login/', LoginView.as_view(), name='auth'),
   path(r'registration/', RegistrationView.as_view(), name='auth'),
]