from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUserRegistration, CustomUserLogin
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class MainPage(LoginRequiredMixin, TemplateView):
    template_name = 'users/main-page.html'
    login_url = 'users:login'