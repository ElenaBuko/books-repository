from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'login.html'


class RegistrationView(TemplateView):
    template_name = 'registration.html'
