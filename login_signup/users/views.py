from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUserRegistration, CustomUserLogin
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class RegisterCreateView(CreateView):
    form_class = CustomUserRegistration
    model = User
    template_name = 'users/register-form.html'
    success_url = '/'
    
    
class LoginView(LoginView):
    form_class = CustomUserLogin
    model = User
    template_name = 'users/login.html'
    success_url = 'users/register.html'