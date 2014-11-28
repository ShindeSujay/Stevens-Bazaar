from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        
    def clean_email(self):
        if (self.cleaned_data.get('email', '')
            .endswith('stevens.edu')):
            return self.cleaned_data.get('email', '')
        
        raise ValidationError("Invalid email address.")

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.firstname = self.cleaned_data['first_name']
        user.lastname = self.cleaned_data['last_name']

        if commit:
            user.save()
            
        return user
