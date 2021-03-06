from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    #
    # is_salvation=forms.BooleanField()
    # is_endtime=forms.BooleanField()
    class Meta:
        model=User
        fields=['username','email','password1','password2',]