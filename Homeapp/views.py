from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'Homeapp/home.html')

def about(request):
    return render(request,'Homeapp/about.html')

# Create your views here.
