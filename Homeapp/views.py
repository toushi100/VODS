from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'Homeapp/home.html')

# Create your views here.
