from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import VideoCreationForm
from .models import Video
from django.views import  View
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
    return render(request,'Videoapp/upload.html',{'form':form})

'''

class upload(View):
    model = Video
    success_url = reverse_lazy('home')

    def get(request,self,*args, **kwargs):
        form = VideoCreationForm()
        return render(request,'Videoapp/upload.html',{'form':form})

    def post(request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(self.Video.video)
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})
'''
def index(request):
    videos = Video.objects.all()
    return render(request,'Videoapp/index.html',{'videos':videos})

class show(DetailView,View):
    model = Video
    template_name = 'Videoapp/show.html'
    success_url = '/'
    def post(request,self,pk):
        print(request)
        video = get_object_or_404(Video, id = pk) 
        os.remove("/home/ahmed/Desktop/VODS/media/{}".format(video.video))
        video.delete()
        return HttpResponseRedirect(reverse('index'))
  
    
        
    
    """

def delete(request, id):  
    context ={} 
    obj = get_object_or_404(Video, id = id) 
    if request.method =="POST": 
        obj.delete() 
        messages.success(request, f' the {video.name} has been deleted successfully')
        return render(redirect, 'Videoapp/video_confirm_delete.html') 
  
    return render(request,'Videoapp/index.html') 
        """