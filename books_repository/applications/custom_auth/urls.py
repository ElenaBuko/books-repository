from . import views
from django.urls import path

from applications.custom_auth.views import CustomRegistrationView

app_name = 'custom_auth'

urlpatterns = [
    path(r'registration/',  CustomRegistrationView.as_view(), name='registration'),
]
