from django.db import models
from  django.contrib.auth.models import User
import time, subprocess, pickle, json
from embed_video.fields import EmbedVideoField 
from django.db.models.signals import post_save




def create_profile(sender,instance,created,**kwargs):
    if created:
        path = '/home/ahmed/Desktop/VODS/filename.pickle'
        video = instance.video
        video = '/home/ahmed/Desktop/VODS/media/'+str(video)
        print("detecting is starting")
        output = subprocess.run(['/home/ahmed/Desktop/SSD/tagroba.py',video])
        with open(path, 'rb') as handle:
            b = pickle.load(handle)
        b = json.dumps(b)
        VideoObject.objects.create(video = instance ,obj = b)
    if not created:
        instance.Videobject.save()

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
        
post_save.connect(create_profile,sender = Video)


                
    
class VideoObject(models.Model):
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
    obj = models.JSONField(null = True)

    def __str__(self):
        return f'{self.video}'


            
            
        
class Commment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    video = models.ForeignKey(Video , on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.comment} on {self.video} by {self.user}'


# def save_profile(sender, instance,created, **kwargs):
#      if not created:
#         instance.Videobject.save()
# post_save.connect(save_profile,sender = Video)
