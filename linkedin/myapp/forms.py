from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from .models import Userprofile

class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True, validators=[
        MinLengthValidator(4, message='Full name should be at least 4 characters long')
    ])
    job_title = forms.CharField(max_length=255, required=True, validators=[
        MinLengthValidator(14, message='Job title should be at least 14 characters long')
    ])

    class Meta:
        model = User
        fields = ['username', 'full_name', 'job_title', 'password1', 'password2']
        
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.full_name = self.cleaned_data["full_name"]
        user.job_title = self.cleaned_data["job_title"]
        if commit:
            user.save()
            Userprofile.objects.create(user=user, full_name=user.full_name, job_title=user.job_title)
        return user     

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
