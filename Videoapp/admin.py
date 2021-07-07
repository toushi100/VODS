from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Video, VideoObject, Commment,Item
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
admin.site.register(Video)
admin.site.register(VideoObject)
admin.site.register(Commment)
