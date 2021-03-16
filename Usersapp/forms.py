from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Layout, Column, Submit, Fieldset


class UserResgisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('first_name', css_class='form-group col-md-6 mb-0'),
    #             Column('last_name', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         'username',
    #         'email',
    #         Row(
    #             Column('password1', css_class='form-group col-md-6 mb-0'),
    #             Column('password2', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         )
    #     )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
