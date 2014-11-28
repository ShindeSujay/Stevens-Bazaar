from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from .models import PostTable

class AdPostForm(forms.ModelForm):
    
    class Meta:
        model = PostTable


 