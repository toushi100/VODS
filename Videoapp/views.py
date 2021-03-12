from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import VideoCreationForm,CommentCreationForm
from .models import Video,VideoObject, Commment
from django.views import View
from django.views.generic import DetailView
from django.urls import reverse
import os ,json


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
    success_url = 'index'

    

    def get(self, request, *args, **kwargs):
        video = Video.objects.get(pk=self.kwargs['pk'])
        comments = Commment.objects.filter(video = self.kwargs['pk'])
        forms = CommentCreationForm()
        print(comments)
        context = {
            'video':video,
            'comments':comments,
            'forms':forms
        }
        return render(request, self.template_name,context)

    def post(self,request,  *args, **kwargs):
        if request.method =="POST":
            if  request.POST.get("delete"):
                video = get_object_or_404(Video, id=self.kwargs['pk'])
                os.remove("/home/ahmed/Desktop/VODS/media/{}".format(video.video))
                video.delete()
                return HttpResponseRedirect(reverse_lazy(self.success_url))

            if  request.POST.get("search"):
                if  request.POST.get("word"):
                    word = request.POST.get("word")
                    video = get_object_or_404(Video, id=self.kwargs['pk'])
                    videoObject = VideoObject.objects.filter(video = video)
                    frames = videoObject[0].obj
                    frames_dict = json.loads(frames)
                    objectframes = frames_dict[word]
                    context = {
                        'video':video,
                    'objectframes': objectframes
                    }
                    return render(request, self.template_name, context)

            if  request.POST.get("comment"):
                forms = CommentCreationForm(request.POST)
                video = get_object_or_404(Video, id=self.kwargs['pk'])
                if forms.is_valid():
                    forms.instance.user = request.user
                    forms.instance.video = video
                    print(forms.instance.comment)
                    forms.save()
                    return HttpResponseRedirect(reverse_lazy(self.success_url))



