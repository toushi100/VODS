from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= "index"),
    #path('upload/',views.upload.as_view(), name= "upload"),
    path('upload/',views.upload, name= "upload"),
    path('show/<int:pk>',views.show.as_view(),name= "show"),
    
]
