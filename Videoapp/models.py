from django.db import models
from  django.contrib.auth.models import User



class Video(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    video = models.FileField(upload_to='Videos',null=True)
    name = models.TextField(max_length=150)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.name} by the user {self.user.first_name}'
    
