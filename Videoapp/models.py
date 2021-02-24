from django.db import models
from  django.contrib.auth.models import User
import time, subprocess, pickle
from embed_video.fields import EmbedVideoField 
from django.db.models.signals import post_save



class Video(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    video = models.FileField(upload_to='Videos')
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=1000)
    uploaded_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.name} by the user {self.user.username}'
    
    def save(self, *args, **kwargs):
        super(Video, self).save(*args, **kwargs)
        video = self.video
        video = '/home/ahmed/Desktop/VODS/media/'+str(video)
        print("detecting is starting")
        output = subprocess.run(['/home/ahmed/Desktop/SSD/tagroba.py',video])
        if output.returncode == 0:
            path = '/home/ahmed/Desktop/SSD/objects.pickle'
            with open(path, 'rb') as handle:
                b = pickle.load(handle)
                print(b)
    
class VideoObject(models.Model):
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
    obj = models.TextField()

    def __str__(self):
        return f'{self.video}'

    '''def save(self, *args, **kwargs):
        video = self.video.video
        video = '/home/ahmed/Desktop/VODS/media/'+str(video)
        output = subprocess.run(['/home/ahmed/Desktop/SSD/tagroba.py',video])
        if output.returncode == 0:
            path = '/home/ahmed/Desktop/SSD/objects.pickle'
            with open(path, 'rb') as handle:
                b = pickle.load(handle)'''



def create_profile(sender,instance,created,**kwargs):
    if created:
        VideoObject.objects.create(video=instance)
        print("object created")

post_save.connect(create_profile,sender = Video)


def save_profile(sender, instance,created, **kwargs):
    if not created:
        instance.Videobject.save()

post_save.connect(save_profile,sender = Video)