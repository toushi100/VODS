from django.contrib import admin

# Register your models here.
from .models import Video, Object

admin.site.register(Video)
admin.site.register(Object)
