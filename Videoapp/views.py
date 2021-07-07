from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import VideoCreationForm,CommentCreationForm
from .models import Video,VideoObject, Commment
from django.views import View
from django.views.generic import DetailView
from django.urls import reverse
from django.core import serializers
import os ,json

final = []

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
        detected_objects = VideoObject.objects.get(
            video =self.kwargs['pk'] )
        
        context = {
            'video':video,
            'comments':comments,
            'forms':forms,
            
        }
        return render(request, self.template_name,context)

    def post(self,request,  *args, **kwargs):
        if request.method =="POST":
            if  request.POST.get("delete"):
                video = get_object_or_404(Video, id=self.kwargs['pk'])
                os.remove("/home/ahmed/Desktop/VODS/media/{}".format(video.video))
                video.delete()
                messages.warning(request, f'Your Video has been Deleted')
                return HttpResponseRedirect(reverse_lazy(self.success_url))

            if  request.POST.get("search"):
                if  request.POST.get("word"):
                    word = request.POST.get("word")
                    word  = word.capitalize()
                    for i, x in enumerate(word):
                        if x == ' ':
                            word = word[:i]
                            break
                   
                    video = get_object_or_404(Video, id=self.kwargs['pk'])
                    videoObject = VideoObject.objects.filter(video = video)
                    frames = videoObject[0].obj
                    frames_dict = json.loads(frames)
                    try:
                        objectframes = frames_dict[word]
                    except KeyError:
                        objectframes = []
                        err = messages.warning(request, f'The object you\'re looking for does not appear in the video \n :( ')
                    if len(objectframes) !=  0:
                        times = [objectframes[0]]
                        for index in range(len(objectframes)-1):
                            if objectframes[index+1] - objectframes[index] == 0:
                                continue
                            elif objectframes[index+1] - objectframes[index] == 1:
                                continue
                            else:
                                times.append(objectframes[index+1])
                        
                        for i in times:
                            seconds = (i / 30);
                            total =  (i % 30)*0.0333;
                            i = seconds+total;
                            final.append(i)
                    context = {
                        'video':video,
                        'objectframes': objectframes,
                        'word':word,
                        'final':final,
                     
                    }
                    return render(request, self.template_name, context)

            if  request.POST.get("comment"):
                forms = CommentCreationForm(request.POST)
                video = get_object_or_404(Video, id=self.kwargs['pk'])
                if forms.is_valid():
                    forms.instance.user = request.user
                    forms.instance.video = video
                    forms.save()
                    return self.get(request)
                    