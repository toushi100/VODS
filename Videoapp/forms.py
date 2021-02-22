from django import forms
from .models import Video

class VideoCreationForm(forms.ModelForm):
    video = forms.FileField()
    name = forms.CharField()
    video.widget.attrs.update({'accept': 'video/mp4','class':'btn btn-info'})
    class Meta:
        model = Video
        fields = ['name', 'description','video']
