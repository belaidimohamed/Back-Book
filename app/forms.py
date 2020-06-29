from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from .models import UserProfile , Friends , Messages
from django.core.files.images import get_image_dimensions


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["username", "password"]

    def clean(self):
        if self.is_valid():
            if not authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password']):
                raise forms.ValidationError('Error, Invalid username or password!')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","email", "password"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profilePicture','sex','bio']
