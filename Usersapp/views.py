from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm

def regesiter(request):
    form = UserCreationForm()
    return render (request, 'Usersapp/regesiter.html', {'form':form})

def dashboard(request):
    return HttpResponse("dashboard")
