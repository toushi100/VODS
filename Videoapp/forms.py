from django import forms
from .models import Video

class VideoCreationForm(forms.ModelForm):
    video = forms.FileField()
    class Meta:
        model = Video
        fields = ['name', 'description']

    def handle_uploaded_file(f):
        with open('/media/videos', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)