from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Profile,Post

class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields = ["username","email","password1","password2"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio","profile_picture"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4, "cols": 50})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["content"]