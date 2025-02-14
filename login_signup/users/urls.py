from django.contrib.auth.views import LogoutView
from django.urls import path 
from . import views 

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterCreateView.as_view(), name='register'),
    path('', views.LoginView.as_view(), name='login'),
    path('main/', views.MainPage.as_view(), name='main-page'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    
]

