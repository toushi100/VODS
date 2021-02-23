from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .forms import UserResgisterForm, UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from Videoapp.models import Video ,User



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




@login_required
def dashboard(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('dashboard')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        uservideos = Video.objects.filter(user= request.user)
        context = {
        'u_form':u_form,
        'p_form':p_form,
        'uservideos': uservideos,

    }
    return render(request, 'Usersapp/dashboard.html', context)
