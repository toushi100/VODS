from django.db import models
from  django.contrib.auth.models import User
import time
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    video = models.FileField(upload_to='Videos', null=True)
    URL = models.FilePathField(null=True)
    name = models.TextField(max_length=150)
    description = models.TextField(max_length=1000)
    uploaded_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.name} by the user {self.user.first_name}'
    
