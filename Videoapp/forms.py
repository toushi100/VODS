from django import forms
from .models import Video, Commment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class VideoCreationForm(forms.ModelForm):
    video = forms.FileField()
    name = forms.CharField()
    video.widget.attrs.update({'accept': 'video/mp4','class':'btn btn-info'})
    class Meta:
        model = Video
        fields = ['name', 'description','video']
        helper = FormHelper()
        helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        helper.form_method = 'POST'
        
class CommentCreationForm(forms.ModelForm):
    comment = forms.CharField()
    comment.widget.attrs.update({'class':''})
    class Meta:
        model = Commment
        fields = ['comment']