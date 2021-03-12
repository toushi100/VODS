from django.shortcuts import render,HttpResponse
from django.contrib import messages

def home(request):
    return render(request,'Homeapp/home.html')

def about(request):
    messages.success(request, f'this is the about page')
    return render(request,'Homeapp/about.html')

# Create your views here.
