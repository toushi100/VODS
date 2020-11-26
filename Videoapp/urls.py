from django.urls import path
from . import views

urlpatterns = [
    path('upload/',views.show, name= "show"),
    

]