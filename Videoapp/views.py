from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import VideoCreationForm
from .models import Video
from django.views.generic import  DetailView

   

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


def index(request):
    videos = Video.objects.all()
    return render(request,'Videoapp/index.html',{'videos':videos})

class show(DetailView):
    model = Video
    template_name = 'Videoapp/show.html'

def video():
    video = Video.video
    return video