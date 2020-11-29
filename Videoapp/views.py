from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import VideoCreationForm



@login_required
def upload(request):
    if request.method == 'POST':
        form = VideoCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, f'Video Uploaded Successfully')
            return redirect('dashboard')
    else:
       form = VideoCreationForm()
    return render(request,'Videoapp/upload.html',{'form':form})


def show(request):
    return render(request,'Videoapp/upload.html')