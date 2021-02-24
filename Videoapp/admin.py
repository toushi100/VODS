from django.contrib import admin

# Register your models here.
from .models import Video, VideoObject

admin.site.register(Video)
admin.site.register(VideoObject)
