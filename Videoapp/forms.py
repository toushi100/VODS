from django import forms
from .models import Video

class VideoCreationForm(forms.ModelForm):
    video = forms.FileField()
    name = forms.CharField()
    class Meta:
        model = Video
        fields = ['name', 'description','video']
