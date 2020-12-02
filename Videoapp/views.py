from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import VideoCreationForm
from .models import Video
from django.views.generic import  DetailView,DeleteView
from django.contrib import messages


   

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

"""class delete(DeleteView):
    model = Video
    success_url = '/'
    def test_func(self):
        video = self.get_object()
        if self.request.user == video.user:
            return True
        return False  
    
    def messages(request):
        messages.success(request, f' the {vidoe.name} has been deleted successfully')"""

def delete(request, id):  
    context ={} 
    obj = get_object_or_404(Video, id = id) 
    if request.method =="POST": 
        obj.delete() 
        messages.success(request, f' the {vidoe.name} has been deleted successfully')
        return HttpResponseRedirect("/") 
  
    return render(request, context) 
        