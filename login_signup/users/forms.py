from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserRegistration(UserCreationForm):
    class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']
      labels = {
          'username': 'Username',
          'email': 'Email',
          'password1': 'Password',
          'password2': 'Confirm Password'
      }
      

class CustomUserLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'placeholder': 'Enter Username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

        