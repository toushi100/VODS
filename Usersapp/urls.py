from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/',views.dashboard, name= "dashboard"),
    path('register/',views.register, name= "register"),
     path('login/', auth_views.LoginView.as_view(template_name='Usersapp/login.html'), name = 'login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='Homeapp/home.html'), name = 'logout'),


    

]