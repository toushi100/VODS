from django.contrib import admin

# Register your models here.
from .models import Video, VideoObject, Commment

admin.site.register(Video)
admin.site.register(VideoObject)
admin.site.register(Commment)
