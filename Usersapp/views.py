from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .forms import UserResgisterForm



def register(request):
    if request.method == 'POST':
        form = UserResgisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = UserResgisterForm()
    return render (request, 'Usersapp/register.html', {'form':form})





def dashboard(request):
    return HttpResponse("dashboard")
