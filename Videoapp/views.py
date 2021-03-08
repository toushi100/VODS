from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import VideoCreationForm
from .models import Video
from django.views import View
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib import messages
import os


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
    return render(request, 'Videoapp/upload.html', {'form': form})


def index(request):
    videos = Video.objects.all()
    count = videos.count()
    return render(request, 'Videoapp/index.html', {'videos': videos})


class show(DetailView, View):
    model = Video
    template_name = 'Videoapp/show.html'
    success_url = '/'

    

    def get(self, request, *args, **kwargs):
        video = Video.objects.get(pk=self.kwargs['pk'])
        return render(request, self.template_name, {'video':video})

    def post(request, self, *args, **kwargs):
        if  self.POST.get("delete"):
            video = get_object_or_404(Video, id=pk)
            os.remove("/home/ahmed/Desktop/VODS/media/{}".format(video.video))
            video.delete()
        if  self.POST.get("search"):
            if  self.POST.get("word"):
                word = self.POST.get("word")
                print(word)
        return HttpResponseRedirect(reverse_lazy('home'))
