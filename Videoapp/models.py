from django.db import models
from  django.contrib.auth.models import User
import time, subprocess, pickle, json
from django.db.models.signals import post_save
from django.conf import settings




def create_profile(sender,instance,created,**kwargs):
    if created:
        path = settings.BASE_DIR/'new.pickle'
        video = instance.video
        video = settings.MEDIA_ROOT+ '/'+ str(video)
        print("detecting is starting")
        output = subprocess.run([settings.BASE_DIR/'SSD/tagroba.py',video])
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
