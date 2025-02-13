from django.urls import path 
from . import views 

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterCreateView.as_view(), name='register'),
    path('', views.LoginView.as_view(), name='login'),
    
]

